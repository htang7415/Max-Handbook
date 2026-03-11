from agent_memory_retrieval import (
    matches_scope,
    retrieve_agent_memories,
    token_overlap_score,
)


def test_token_overlap_and_scope_rules():
    assert token_overlap_score("hybrid search docs", "Use hybrid search for docs") > 0.9
    assert matches_scope({"workspace_id": 7, "agent_id": None}, 7, "agent-1")
    assert not matches_scope({"workspace_id": 8, "agent_id": None}, 7, "agent-1")
    assert not matches_scope({"workspace_id": 7, "agent_id": "agent-2"}, 7, "agent-1")


def test_retrieval_prefers_recent_relevant_memories_in_scope():
    memories = [
        {
            "id": "m1",
            "workspace_id": 7,
            "agent_id": None,
            "text": "Use hybrid search for support docs",
            "created_at": 180,
            "importance": 0.6,
        },
        {
            "id": "m2",
            "workspace_id": 7,
            "agent_id": "agent-1",
            "text": "Support docs need hybrid search plus reranking",
            "created_at": 195,
            "importance": 0.9,
        },
        {
            "id": "m3",
            "workspace_id": 7,
            "agent_id": "agent-2",
            "text": "Private note for another agent",
            "created_at": 199,
            "importance": 1.0,
        },
        {
            "id": "m4",
            "workspace_id": 8,
            "agent_id": None,
            "text": "Other tenant memory",
            "created_at": 199,
            "importance": 1.0,
        },
    ]

    top = retrieve_agent_memories(
        "hybrid search support docs",
        memories,
        workspace_id=7,
        agent_id="agent-1",
        now=200,
        top_k=2,
    )

    assert [memory_id for memory_id, _ in top] == ["m2", "m1"]


def test_min_score_drops_weak_memories():
    memories = [
        {
            "id": "m1",
            "workspace_id": 7,
            "agent_id": None,
            "text": "How to cook pasta",
            "created_at": 199,
        }
    ]

    assert (
        retrieve_agent_memories(
            "hybrid search support docs",
            memories,
            workspace_id=7,
            agent_id="agent-1",
            now=200,
            top_k=1,
            min_score=0.3,
        )
        == []
    )
