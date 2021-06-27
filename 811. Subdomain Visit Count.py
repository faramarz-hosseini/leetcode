class Solution:
    def find_dot_indexes(self, string):
        dot_indexes = []
        for i in range(len(string)):
            if string[i] == '.':
                dot_indexes.append(i)

        return dot_indexes[::-1]

    def make_subdomain(self, domain):
        sub_domains = []
        dot_indexes = self.find_dot_indexes(domain)
        sub_domains_count = len(dot_indexes) + 1
        dot_index_pointer = 0

        for sub in range(sub_domains_count):
            sub_domain = ''

            for index in range(len(domain) - 1, -1, -1):

                if dot_index_pointer > len(dot_indexes) - 1:
                    break

                if index == dot_indexes[dot_index_pointer]:
                    dot_index_pointer += 1
                    sub_domains.append(sub_domain[::-1])
                    break

                sub_domain += domain[index]

        return sub_domains + [domain]

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = {}

        for entry in cpdomains:
            visit_count = int(entry.split()[0])
            domain = entry.split()[1]

            sub_domains = self.make_subdomain(domain)
            print(sub_domains)
            for sub in sub_domains:
                if visits.get(sub) is not None:
                    visits[sub] += visit_count
                else:
                    visits[sub] = visit_count

        return self.generate_output(visits)

    def generate_output(self, dictionary):
        output = []
        entry = ''

        for sub, visit in dictionary.items():
            entry += str(visit) + " " + sub
            output.append(entry)
            entry = ''

        return output
