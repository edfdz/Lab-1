from timeit import default_timer as timer

    
my_set = set(line.strip() for line in open('words_alpha.txt'))
  

word_set = set([])
prefix_set = set([])
permutation_set = set([])

def findAnagram(word,temp):
    if len(word) == 0:
        if temp in my_set and temp != word and temp not in word_set:
            word_set.add(temp)
    else:
        for i in range(len(word)):
            scrambles = word[i]
            remaining = word[:i] + word [i+1:]
            if (temp + scrambles) in prefix_set:
                findAnagram(remaining, temp + scrambles)
           
def findAnagramP1(word,temp):
 if len(word) == 0:
     for i in my_set:
         if temp == i:
             word_set.add(temp)
 else:
     for i in range(len(word)):
         scrambles = word[i]
         remaining = word[:i] + word [i+1:]
         findAnagramP1(remaining, temp + scrambles)    
          
def prefix2 ():
    for i in my_set:
        for j in range(1,len(i)):
                prefix = i[:j-1]
                prefix_set.add(prefix)
               
                

        
             
word = input('Enter a word or empty string to finish: ')

start = timer()
prefix2()
findAnagram(word,'')
print (sorted(word_set))
end = timer()
print('Runtime:',str(end-start))
     


