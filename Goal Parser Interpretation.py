class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        output = ''
        for i in range(len(command)):
            if command[i] == '(':
                if command[i+1] != 'a':
                    output += 'o'
                else:
                    output += 'al'
            elif command[i] == "G":
                output += "G"

        return output
