# class Solution:
from typing import List
def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    wordLen = 0;
    result = [];
    lines = [];
    str = [];
    for word in words:
        if wordLen + len(word) < maxWidth:
            str.append(word);
            wordLen += len(word) + 1;
        else:
            lines.append(str);
            str = [word];
            wordLen = len(word) + 1;
    for line in lines:
        wordLen = 0;
        for word in line:
            wordLen += len(word);
        blankNum = 0;
        extraNum = 0;
        if len(line) > 1:
            blankNum = int((maxWidth - wordLen) / (len(line) - 1));
            extraNum = maxWidth - blankNum * (len(line) - 1) - wordLen;
        else:
            blankNum = maxWidth - wordLen;
        outLine = '';
        for word in line[:len(line) - 1]:
            outLine += word;
            for i in range(blankNum):
                outLine +=' ';
            if extraNum > 0:
                outLine +=' ';
                extraNum -= 1;
        outLine += line[len(line) - 1];
        result.append(outLine);

    return result;


print(fullJustify(["What","must","be","acknowledgment","shall","be"],16));
print(fullJustify(["Science","is","what","we","understand","well","enough","to","explain", "to","a","computer.","Art","is","everything","else","we","do"],20));