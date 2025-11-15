class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = {}

        def find(x):
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return parents[x]
        
        def union(x, y):
            parents[find(x)] = parents[find(y)]

        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                email_to_name[email] = name
                if email not in parents:
                    parents[email] = email
                union(first_email, email)

        merged_accounts = defaultdict(list)
        for email in parents:
            root = find(email)
            merged_accounts[root].append(email)

        result = [[email_to_name[root]] + sorted(emails) for root, emails in merged_accounts.items()]
        return result
