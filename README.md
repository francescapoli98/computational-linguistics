# Progetto d'esame di Linguistica Computazionale - A.A. 2018/2019
\[english below]
## Obiettivo:
Realizzazione di due programmi scritti in Python che utilizzino i moduli presenti in **Natural Language Toolkit (NLTK)** per leggere due file di testo in inglese, annotarli linguisticamente, confrontarli sulla base degli indici statistici richiesti ed estrarne le informazioni richieste.
## Fasi di realizzazione:
Creazione due corpora in inglese, di almeno 5000 token ciascuno, contenenti testi estratti rispettivamente da commenti positivi e negativi di prodotti o servizi venduti su siti on-line. I commenti sono distinti tra positivi e negativi sulla base delle meta informazioni che ogni sito predispone vicino ai commenti. I corpora sono salvati in due file di testo semplice in codifica utf-8. Sono sviluppati poi due programmi che prendono in input i due file da riga di comando, che li analizzano linguisticamente fino al Part-of-Speech tagging e che eseguono le operazioni richieste.

### Programma 1 - Confronto dei due testi sulla base delle seguenti informazioni statistiche:
* il numero totale di frasi e di token;
* la lunghezza media delle frasi in termini di token e la lunghezza media delle parole in termini di caratteri;
* la grandezza del vocabolario e la Type Token Ratio (TTR) all'aumentare del corpus per porzioni incrementali di 1000 token;
* la grandezza delle classi di frequenza |V3|, |V6| e |V9| sui primi 5000 token;
* il numero medio di Sostantivi, Aggettivi e Verbi per frase.
* la densità lessicale, calcolata come il rapporto tra il numero totale di occorrenze nel testo di Sostantivi, Verbi, Avverbi, Aggettivi e il numero totale di parole nel testo (ad esclusione dei segni di punteggiatura marcati con POS "," "."):
(|Sostantivi|+|Verbi|+|Avverbi|+|Aggettivi|)/(TOT-( |.|+|,| ) ).

### Programma 2 - Per ognuno dei due corpora sono estratte le seguenti informazioni:
* estratti ed ordinati in ordine di frequenza decrescente, indicando anche la relativa frequenza:
  * i 20 token più frequenti escludendo la punteggiatura;
  * i 20 Sostantivi più frequenti;
  * i 20 Aggettivi più frequenti;
  * i 20 bigrammi di token più frequenti che non contengono punteggiatura, articoli e congiunzioni;
  * le 10 PoS (Part-of-Speech) più frequenti;
  * i 10 bigrammi di PoS (Part-of-Speech) più frequenti;
  * i 10 trigrammi di PoS (Part-of-Speech) più frequenti;
* estratti ed ordinati in ordine decrescente i 20 bigrammi composti da Aggettivo e Sostantivo (dove ogni token deve avere una frequenza maggiore di 2):
  * con frequenza massima, indicando anche la frequenza di ogni parola che compone il bigramma;
  * con probabilità congiunta massima, indicando anche la relativa probabilità;
  * con forza associativa massima (calcolata in termini di Local Mutual Information), indicando anche il relativo valore;
* le due frasi con probabilità più alta, dove la probabilità della prima frase deve essere calcolata attraverso un modello di Markov di ordine 0 mentre la seconda con un modello di Markov di ordine 1. I due modelli devono usare le distribuzioni di frequenza estratte dal corpus che contiene le frasi, le frasi devono essere lunghe minimo 6 e massimo 8 token e ogni token deve avere una frequenza maggiore di 2;

## Risultati del progetto:
* i due file di testo contenenti i corpora (*positive_reviews.txt* e *negative_reviews.txt*);
* i programmi commentati in Python 2.7 (*programma1.py* e *programma2.py*);
* i file di testo contenenti l'output dei programmi (*output1.txt* e *output2.txt*).

------

# Computational Linguistics Examination Project - A.A. 2018/2019.
## Objective:
Implementation of two programs written in Python using the modules present in **Natural Language Toolkit (NLTK)** to read two English text files, annotate them linguistically, compare them based on the required statistical indices and extract the required information.
## Implementation phases:
Creation of two English corpora, of at least 5000 tokens each, containing texts extracted respectively from positive and negative comments on products or services sold on online sites. The comments are distinguished between positive and negative on the basis of the meta information that each site places next to the comments. The corpora are saved in two plain text files in utf-8 encoding. Two programs are then developed that take the two files as input from the command line, that linguistically analyse them up to Part-of-Speech tagging and that perform the required operations.

### Program 1 - Comparison of the two texts based on the following statistical information:
* the total number of sentences and tokens;
* the average length of the sentences in terms of tokens and the average length of the words in terms of characters;
* the size of the vocabulary and the Type Token Ratio (TTR) as the corpus increases for incremental portions of 1000 tokens;
* the size of the frequency classes |V3|, |V6| and |V9| over the first 5000 tokens;
* the average number of Nouns, Adjectives and Verbs per sentence.
* lexical density, calculated as the ratio between the total number of occurrences in the text of Nouns, Verbs, Adverbs, Adjectives and the total number of words in the text (excluding punctuation marks marked with POS "," "."):
(|Substantives|+|Verbs|+|Adjectives|)/(TOT-( |.|+|,| ) ).

### Program 2 - For each of the two corpora, the following information is extracted:
* extracted and sorted in order of decreasing frequency, also indicating the relative frequency:
  * the 20 most frequent tokens excluding punctuation;
  * the 20 most frequent nouns;
  * the 20 most frequent adjectives;
  * the 20 most frequent token bigrams not containing punctuation, articles and conjunctions;
  * the 10 most frequent PoS (Part-of-Speech);
  * the 10 most frequent PoS (Part-of-Speech) bigrams;
  * the 10 most frequent PoS (Part-of-Speech) trigrams;
* extracted and ordered in descending order the 20 bigrams composed of Adjective and Noun (where each token must have a frequency greater than 2):
  * with maximum frequency, indicating also the frequency of each word composing the bigram;
  * with maximum joint probability, indicating also the relative probability;
  * with maximum associative strength (calculated in terms of Local Mutual Information), indicating also the relative value;
* the two sentences with the highest probability, where the probability of the first sentence has to be calculated through a Markov model of order 0 while the second with a Markov model of order 1. The two models have to use the frequency distributions extracted from the corpus containing the sentences, the sentences have to be minimum 6 and maximum 8 tokens long and each token has to have a frequency greater than 2;

## Project results:
* the two text files containing the corpora (*positive_reviews.txt* and *negative_reviews.txt*);
* the commented programs in Python 2.7 (*program1.py* and *program2.py*);
* the text files containing the output of the programs (*output1.txt* and *output2.txt*).
