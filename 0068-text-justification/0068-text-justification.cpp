class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> result;
        int index = 0;

        while (index < words.size()) {
            int lineLength = 0;
            vector<string> lineWords;

            // Collect words for the current line
            while (index < words.size() && lineLength + words[index].size() + lineWords.size() <= maxWidth) {
                lineWords.push_back(words[index]);
                lineLength += words[index].size();
                index++;
            }

            string justifiedLine = "";
            if (index < words.size() && lineWords.size() > 1) {
                // Full justification for non-last lines
                int totalSpaces = maxWidth - lineLength;
                int spacesBetween = totalSpaces / (lineWords.size() - 1);
                int extraSpaces = totalSpaces % (lineWords.size() - 1);

                for (int i = 0; i < lineWords.size(); i++) {
                    justifiedLine += lineWords[i];
                    if (i < lineWords.size() - 1) {
                        justifiedLine += string(spacesBetween, ' ');
                        if (extraSpaces > 0) {
                            justifiedLine += " ";
                            extraSpaces--;
                        }
                    }
                }
            } else {
                // Left justification for the last line or single-word lines
                for (int i = 0; i < lineWords.size(); i++) {
                    justifiedLine += lineWords[i];
                    if (i < lineWords.size() - 1) justifiedLine += " ";
                }
                justifiedLine += string(maxWidth - justifiedLine.size(), ' ');
            }

            result.push_back(justifiedLine);
        }

        return result;
    }
};
