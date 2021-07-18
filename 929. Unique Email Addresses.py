class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_list = {}

        for em in emails:
            local, domain = em.split("@")
            refined_local = self.refine_local_email(local)

            final_email = refined_local + "@" + domain
            email_list[final_email] = True

        return len(email_list)

    def refine_local_email(self, local_email):
        refined = ""
        for letter in local_email:
            if letter == "+":
                break
            if letter != '.':
                refined += letter

        return refined
