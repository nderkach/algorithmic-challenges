class Solution(object):

    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num_map = {
            "6": "9",
            "9": "6",
            "8": "8",
            "1": "1",
            "0": "0"
        }

        string = str(num)
        i = 0
        j = len(string) - 1

        while i < j:
            if string[i] in num_map and num_map[string[i]] == string[j]:
                i += 1
                j -= 1
            else:
                return False

        if i == j and string[i] not in ('1', '8', '0'):
            return False
        else:
            return True
