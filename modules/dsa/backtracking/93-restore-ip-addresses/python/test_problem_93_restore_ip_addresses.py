from problem_93_restore_ip_addresses import Solution


def test_restore_ip_addresses_example():
    result = Solution().restoreIpAddresses("25525511135")
    assert sorted(result) == ["255.255.11.135", "255.255.111.35"]


def test_restore_ip_addresses_edge_short():
    assert Solution().restoreIpAddresses("1111") == ["1.1.1.1"]


def test_restore_ip_addresses_tricky_leading_zeroes():
    assert sorted(Solution().restoreIpAddresses("010010")) == ["0.10.0.10", "0.100.1.0"]
