file = open('input.txt', 'r')
sentence = "".join(file.readlines())

def calculate_frequencies():
    # here is a list of punctuations and uninteresting words you can use
    # to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    def create_dictionary(file_contents):
        result = {}
        for word in file_contents.split():
            if word in uninteresting_words:
                continue
            else:
                if word.isalpha():
                    for letter in word:
                        if letter in punctuations:
                            letter.replace(punctuations, '')
                    if word not in result:
                        result[word] = 0
                    result[word] += 1
        return result

    frequencies = create_dictionary(sentence)
    print(sentence)
    print(frequencies)


calculate_frequencies()