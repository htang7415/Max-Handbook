import MarkdownRenderer from "./MarkdownRenderer";

interface FirstPrinciplesPanelProps {
  title: string;
  summary?: string;
  intro?: string;
  purpose?: string;
  math?: string;
  keypoints?: string;
  hasCode: boolean;
  hasVisual: boolean;
}

function stripMarkdown(text: string) {
  return text
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/\$\$([\s\S]*?)\$\$/g, (_match, inner: string) => inner)
    .replace(/\$([^$]+)\$/g, (_match, inner: string) => inner)
    .replace(/!\[[^\]]*\]\([^)]*\)/g, " ")
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
    .replace(/`([^`]*)`/g, "$1")
    .replace(/^[#>\-*+]+\s*/gm, "")
    .replace(/\s+/g, " ")
    .trim();
}

function firstSentence(text?: string, maxLength = 170) {
  if (!text) return undefined;
  const cleaned = stripMarkdown(text);
  if (!cleaned) return undefined;
  const match = cleaned.match(/(.+?[.!?])(\s|$)/);
  const sentence = match ? match[1].trim() : cleaned;
  if (sentence.length <= maxLength) return sentence;
  return `${sentence.slice(0, maxLength - 1).trimEnd()}...`;
}

function firstEquation(text?: string) {
  if (!text) return undefined;
  const display = text.match(/\$\$([\s\S]*?)\$\$/);
  if (display) {
    return display[1].replace(/\s+/g, " ").trim();
  }
  const inline = text.match(/\$([^$]+)\$/);
  if (inline) {
    return inline[1].replace(/\s+/g, " ").trim();
  }
  return firstSentence(text, 120);
}

function firstEquationMarkdown(text?: string) {
  if (!text) return undefined;
  const display = text.match(/\$\$([\s\S]*?)\$\$/);
  if (display) {
    return `$$\n${display[1].trim()}\n$$`;
  }
  const inline = text.match(/\$([^$]+)\$/);
  if (inline) {
    return `$$\n${inline[1].trim()}\n$$`;
  }
  return undefined;
}

function hasMarkdownList(text?: string) {
  return Boolean(text && /^\s*([-*+]|\d+\.)\s+/m.test(text));
}

export default function FirstPrinciplesPanel({
  title,
  summary,
  intro,
  purpose,
  math,
  keypoints,
  hasCode,
  hasVisual,
}: FirstPrinciplesPanelProps) {
  const question =
    firstSentence(purpose, 155) ??
    firstSentence(summary, 155) ??
    `Understand the core job of ${title.toLowerCase()}.`;
  const mechanismMarkdown = hasMarkdownList(intro) && intro ? intro.trim() : undefined;
  const mechanism =
    mechanismMarkdown ??
    firstSentence(intro, 165) ??
    firstSentence(summary, 165) ??
    "Break the transformation into small, inspectable steps.";
  const mechanismKind = mechanismMarkdown ? "markdown" : "text";
  const equationMarkdown = firstEquationMarkdown(math);
  const equation =
    equationMarkdown ??
    firstEquation(math) ??
    "Track how the input is transformed and what stays invariant.";
  const verifyMarkdown =
    !hasVisual && !hasCode && hasMarkdownList(keypoints) ? keypoints?.trim() : undefined;
  const verify = hasVisual
    ? "Use the visual below to connect the update rule to the behavior."
    : hasCode
      ? "Run the code below on a tiny example and compare the output to the rule."
      : verifyMarkdown ??
        firstSentence(keypoints, 165) ??
        "Check the invariants: what changes, what is preserved, and why.";

  const cards = [
    { step: "01", label: "Question", text: question, tone: "question", kind: "text" },
    {
      step: "02",
      label: "Mechanism",
      text: mechanism,
      tone: "mechanism",
      kind: mechanismKind,
    },
    {
      step: "03",
      label: "Equation",
      text: equation,
      tone: "equation",
      kind: equationMarkdown ? "math" : "text",
    },
    {
      step: "04",
      label: "Verify",
      text: verify,
      tone: "verify",
      kind: verifyMarkdown ? "markdown" : "text",
    },
  ];

  return (
    <section className="first-principles-panel" aria-label="First principles map">
      <div className="first-principles-header">
        <div>
          <div className="first-principles-eyebrow">First principles</div>
          <h3>{title}</h3>
        </div>
        <p>
          Start from the core question, follow the mechanism, then use the
          equation and code to verify your mental model.
        </p>
      </div>

      <div className="first-principles-grid">
        {cards.map((card) => (
          <article
            key={card.step}
            className={`first-principles-card first-principles-card-${card.tone}`}
          >
            <div className="first-principles-card-head">
              <div className="first-principles-step">{card.step}</div>
              <div className="first-principles-label">{card.label}</div>
            </div>
            {card.kind === "math" ? (
              <div className="first-principles-math">
                <MarkdownRenderer content={card.text} />
              </div>
            ) : card.kind === "markdown" ? (
              <div className="first-principles-rich">
                <MarkdownRenderer content={card.text} />
              </div>
            ) : (
              <p>{card.text}</p>
            )}
          </article>
        ))}
      </div>
    </section>
  );
}
