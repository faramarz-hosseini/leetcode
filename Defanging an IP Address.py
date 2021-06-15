class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result = ""
        for char in address:
            if char == ".":
                result += "[.]"
            else:
                result += char

        return result