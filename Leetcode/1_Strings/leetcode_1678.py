class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()","o").replace("(al)","al")

#         i = 0
#         output = ""
        
#         while i < len(command):
#             if command[i] == "G":
#                 output += "G"
#                 i += 1
#             elif command[i] == "(" and command[i+1]== ")":
#                 output += "o"
#                 i += 2
#             else:
#                 output += "al"
#                 i += 4
#         return output