#-*- coding: utf-8 -*-
import sys
import codecs
import nltk
import math
from nltk import bigrams
from nltk import trigrams

#POS TAGGER
def AnnotazioneLing(frasi):
    tokensTOT = []
    tokensPOStot = []
    for frase in frasi:
        frase = frase.encode('utf-8')
        tokens = nltk.word_tokenize(frase)
        tokensPOS = nltk.pos_tag(tokens)
       #primo elmento della coppia: token
        tokensTOT = tokensTOT + tokens
       #secondo elemento della coppia: analisi morfosintattica
        tokensPOStot = tokensPOStot + tokensPOS
    return tokensTOT, tokensPOStot

def EstraiSequenza(AnalyzedText):
    listaPOS = []
    for bigramma in AnalyzedText:
        #per inserire elementi in coda alla listaPOS
        listaPOS.append(bigramma[1])
    return listaPOS

#creo un dizionario 
def dizionario(lista):
    dictionary = {}
    vocabolario = set(lista)
    for elem in vocabolario:
        freq = lista.count(elem)
        dictionary[elem] = freq
    return dictionary

#ordino il dizionario
def ordina(dict):
    return sorted(dict.items(), key = lambda x: x[1], reverse=True)

#elimino la punteggiatura dalla lista di token
def nopunteggiatura(lista):
    tokens = []
    for token in lista:
        if (token not in [".",",","?","!",":",";","(",")","-"]):
            tokens.append(token)
    return tokens

#prendo i nomi dalla lista di token/POS
def estrainomi(lista):
    listanomi = []
    for bigramma in lista:
        if (bigramma[1] in ["NNP","NNPS","NN","NNS"]):
            listanomi.append(bigramma[0])
    return listanomi

#prendo gli aggettivi
def estraiagg(lista):
    listaagg = []
    for bigramma in lista:
        if (bigramma[1] in ["JJ","JJS","JJR"]):
            listaagg.append(bigramma[0])
    return listaagg

#seleziono i token da analizzare
def estraitokens(lista):
    nuovalista = []
    for elem in lista:
        if ((elem[0][1] not in  [".",",","?","!",":",";","(",")","-","CC","IN","DT"]) and (elem[1][1] not in  [".",",","?","!",":",";","(",")","-","CC","IN","DT"])):
            nuovalista.append(elem)
    return nuovalista

#estraggo sia gli aggettivi che i sostantivi
def estraiAggSos(lista):
    bigrammi = []
    listabigr =list(bigrams(lista))
    for bigramma in listabigr:
        if ((bigramma[0][1] in ['JJ','JJS','JJR']) and (bigramma[1][1] in ['NN','NNP','NNS','NNPS'])):
            bigrammi.append(bigramma)
    return bigrammi   

def selectAS(lista):
    nomiagg = []
    for bigramma in lista:
        freq = lista.count(bigramma)
        if freq > 2:
            if ((bigramma[1] in ['JJ','JJS','JJR']) or (bigramma[1] in ['NN','NNS','NNP','NNPS'])):
                nomiagg.append(bigramma)
    return nomiagg

def prendibigrammi(lista):
    listabigrammi = []
    for elem in lista:
        bigramma = elem[0]
        listabigrammi.append(bigramma)
    return listabigrammi

def Markov0(corpus, freqtoken, frase):
    prob = 1.0
    probTokenTOT = {}                 #dizionario con le coppie token-probabilità
    for token in frase :
        probToken = (freqtoken[token]*1.0 / corpus*1.0)    #calcolo la probablità dei singoli token 
        prob = prob*probToken                              #moltiplico tutte le probabilità tra loro (eventi indipendenti)
        probTokenTOT[token] = probToken                    
    return prob, probTokenTOT 

def Markov1(corpus, freqtoken, frase):
    prob= 1.0
    fraserange = frase[1:len(frase)]
    bigrammiFrase = list(bigrams(fraserange))    #prendo i bigrammi della frase e del testo completo per confrontarli e calcolare le frequenze
    bigrammiTesto = list(bigrams(corpus))
    token = frase[1]
    probToken = (freqtoken[token]*1.0 / len(corpus)*1.0)    
    for bigramma in bigrammiFrase:
        freqBigramma = bigrammiTesto.count(bigramma)  #calcolo frequenze
        A = bigramma[0]
        probCond = (freqBigramma*1.0 / corpus.count(A)*1.0 )  #calcolo la probabilità condizionata del bigramma
        prob = prob * probCond                                #moltiplico le n probabilità condizionate, e nel return moltiplico il tutto per il primo token la cui probabilità non è condizionata
    return  prob*probToken
        


    
def main(file1,file2):
    fileInput1=codecs.open(file1,'r','utf-8')
    raw1=fileInput1.read()
    fileInput2=codecs.open(file2,'r','utf-8')
    raw2=fileInput2.read()
    sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    frasi1 = sent_tokenizer.tokenize(raw1)
    frasi2 = sent_tokenizer.tokenize(raw2)
#POS TAGGER
   #chiamo la funzione che fa il POS tagging
    TokenizedText1, AnalyzedText1 = AnnotazioneLing(frasi1)
    TokenizedText2, AnalyzedText2 = AnnotazioneLing(frasi2)
   #chiamo la funzione che crea la sequenza token-tag
    SequenzaPOS1 = EstraiSequenza(AnalyzedText1)
    SequenzaPOS2 = EstraiSequenza(AnalyzedText2)
#PRIMI 20 TOKEN
   #POSITIVE
    listatoken1 = nopunteggiatura(TokenizedText1) #creo una lista di tutti i token esclusa la punteggiatura
    listabigrammi1 = dizionario(listatoken1) #creo un dizionario dei token con annessa la frequenza
    listaordinata1 = ordina(listabigrammi1) #ordino il dizionario secondo la frequenza decrescente
   #NEGATIVE
    listatoken2 = nopunteggiatura(TokenizedText2)
    listabigrammi2 = dizionario(listatoken2)
    listaordinata2 = ordina(listabigrammi2)
    print "\n\tI primi 20 token più frequenti:\nPOSITIVE:\n"
    for elem in listaordinata1[0:20]:
        print "Token:\t", elem[0], "\nFrequenza:\t", elem[1], "\n"
    print "\nNEGATIVE:\n"
    for elem in listaordinata2[0:20]:
        print "Token:\t", elem[0], "\nFrequenza:\t", elem[1], "\n"
#PRIMI 20 SOSTANTIVI 
   #POSITIVE
    bigrammiNome1 = estrainomi(AnalyzedText1) #creo una lista con i soli bigrammi nome
    dictNomi1 = dizionario(bigrammiNome1)  #creo il dizionario con i nomi postaggati e la frequenza di ogni bigramma
    dictNomiOrdinato1 = ordina(dictNomi1) #ordino il dizionario secondo la frequenza decrescente
   #NEGATIVE
    bigrammiNome2 = estrainomi(AnalyzedText2)
    dictNomi2 = dizionario(bigrammiNome2)
    dictNomiOrdinato2 = ordina(dictNomi2)
    print "\n\tI primi 20 sostantivi più frequenti:\nPOSITIVE:\n"
    for elem in dictNomiOrdinato1[0:20]:
        print "Sostantivo:\t", elem[0], "\nFrequenza:\t", elem[1], "\n"
    print "\nNEGATIVE:\n"
    for elem in dictNomiOrdinato2[0:20]:
        print "Sostantivo:\t", elem[0], "\nFrequenza:\t", elem[1], "\n"
#PRIMI 20 AGGETTIVI
   #POSITIVE
    bigrammiAgg1 = estraiagg(AnalyzedText1)
    dictAgg1 = dizionario(bigrammiAgg1)
    dictAggOrdinato1 = ordina(dictAgg1)
   #NEGATIVE
    bigrammiAgg2 = estraiagg(AnalyzedText2)
    dictAgg2 = dizionario(bigrammiAgg2)
    dictAggOrdinato2 = ordina(dictAgg2)
    print "\n\tI primi 20 aggettivi più frequenti:\nPOSITIVE:\n"
    for elem in dictAggOrdinato1[0:20]:
        print "Aggettivo:\t", elem[0], "\nFrequenza:\t", elem[1], "\n"
    print "\nNEGATIVE:\n"
    for elem in dictAggOrdinato2[0:20]:
        print "Aggettivo:\t", elem[0], "\nFrequenza:\t", elem[1], "\n"  
#PRIMI 20 BIGRAMMI DI TOKEN SENZA PUNTEGGIATURA, ARTICOLI E CONGIUNZIONI
   #POSITIVE
    bigrammiditoken1 = list(bigrams(AnalyzedText1))
    bigrammiTokenPuliti1 = estraitokens(bigrammiditoken1)
    dictTokens1 = dizionario(bigrammiTokenPuliti1)
    dictTokensOrdinato1 = ordina(dictTokens1)
   #NEGATIVE
    bigrammiditoken2 = list(bigrams(AnalyzedText2))
    bigrammiTokenPuliti2 = estraitokens(bigrammiditoken2)
    dictTokens2 = dizionario(bigrammiTokenPuliti2)
    dictTokensOrdinato2 = ordina(dictTokens2)
    print "\n\tI 20 bigrammi di token più frequenti, esclusi punteggiatura, articoli e congiunzioni:\nPOSITIVE:\n"
    for elem in dictTokensOrdinato1[0:20]:
        print "Chiave:\t", elem[0], "\nValore:\t", elem[1], "\n"
    print "\nNEGATIVE:\n"
    for elem in dictTokensOrdinato2[0:20]:
        print "Chiave:\t", elem[0], "\nValore:\t", elem[1], "\n"
#10 POS PIU' FREQUENTI
   #POSITIVE
    POS1 = []
    for bigramma in AnalyzedText1:
        POS1.append(bigramma[1])
    dictPOS1 = dizionario(POS1)
    dictPOSOrdinato1 = ordina(dictPOS1)
   #NEGATIVE
    POS2 = []
    for bigramma in AnalyzedText2:
        POS2.append(bigramma[1])
    dictPOS2 = dizionario(POS2)
    dictPOSOrdinato2 = ordina(dictPOS2)
    print "\nI primi 10 Part-Of-Speech più frequenti:\nPOSITIVE:\n"
    for elem in dictPOSOrdinato1[0:10]:
        print "POS:\t", elem[0], "\tFrequenza:\t", elem[1]
    print "\nNEGATIVE:\n"
    for elem in dictPOSOrdinato2[0:10]:
        print "POS:\t", elem[0], "\tFrequenza:\t", elem[1]
#10 BIGRAMMI DI POS PIÙ FREQUENTI
   #POSITIVE
    POSbigrams1 = list(bigrams(POS1))
    dictPOSbigrams1 = dizionario(POSbigrams1)
    POSbigramsOrdinato1 = ordina(dictPOSbigrams1)
   #NEGATIVE
    POSbigrams2 = list(bigrams(POS2))
    dictPOSbigrams2 = dizionario(POSbigrams2)
    POSbigramsOrdinato2 = ordina(dictPOSbigrams2)
    print "\n\tI 10 bigrammi di POS più frequenti:\nPOSITIVE:\n"
    for elem in POSbigramsOrdinato1[0:10]:
        print "Chiave:\t", elem [0], "\tValore:\t", elem[1]
    print "\nNEGATIVE:\n"
    for elem in POSbigramsOrdinato2[0:10]:
        print "Chiave:\t", elem [0], "\tValore:\t", elem[1]
#10 TRIGRAMMI DI POS PIU' FREQUENTI
   #POSITIVE
    POStrigrams1 = list(trigrams(POS1))
    frequenzaTrigrammi1 = nltk.FreqDist(POStrigrams1)
    trigrammi1 = frequenzaTrigrammi1.most_common(len(frequenzaTrigrammi1))
   #NEGATIVE
    POStrigrams2 = list(trigrams(POS2))
    frequenzaTrigrammi2 = nltk.FreqDist(POStrigrams2)
    trigrammi2 = frequenzaTrigrammi2.most_common(len(frequenzaTrigrammi2))
    print "\n\tI primi 10 trigrammi di POS in ordine di frequenza decrescente:\nPOSITIVE:\n"
    for elem in trigrammi1[0:10]:
        print  elem[0], "\toccorrenza:\t", elem[1]
    print "\nNEGATIVE:\n"
    for elem in trigrammi2[0:10]:
        print elem[0], "\toccorrenza:\t", elem[1]
#PRIMI 20 BIGRAMMI AGGETTIVO/SOSTANTIVO CON FREQUENZA DEI TOKEN > 2
    print "\n\n\tI primi 20 bigrammi Aggettivo-Sostantivo dei corpora:"
#FREQUENZA MASSIMA
   #POSITIVE
    selezionaAS1 = selectAS(AnalyzedText1)      #prendo tutti i nomi e gli aggettivi dal testo postaggato, che abbiano frequenza>2
    bigrammiAS1 = estraiAggSos(selezionaAS1)    #lista di bigrammi agg-sos (senza frequenza)
    dictAggSos1 = dizionario(bigrammiAS1)       #dizionario dei bigrammi: bigrammi + frequenza del bigramma
    AggSosOrdinati1 = list(ordina(dictAggSos1)) #dizionario ordinato 
    print "\nPer frequenza massima:\nPOSITIVE:\n"
    for elem in AggSosOrdinati1[0:20]:
        jj = elem[0][0]
        nn = elem[0][1]
        print "\nBigramma:\t",elem[0],"\tFrequenza del bigramma:\t", elem[1], "\nAggettivo:", jj,"\tFrequenza assoluta:", AnalyzedText1.count(jj),"\tNome:", nn,"\tFrequenza assoluta:", AnalyzedText1.count(nn), "\n"
   #NEGATIVE
    selezionaAS2 = selectAS(AnalyzedText2)     
    bigrammiAS2 = estraiAggSos(selezionaAS2)   
    dictAggSos2 = dizionario(bigrammiAS2)      
    AggSosOrdinati2 = list(ordina(dictAggSos2))
    print "\nNEGATIVE:\n"
    for elem in AggSosOrdinati2[0:20]:
        jj = elem[0][0]
        nn = elem[0][1]
        print "\nBigramma:\t",elem[0],"\tFrequenza del bigramma:\t", elem[1], "\nAggettivo:", jj,"\tFrequenza assoluta:", AnalyzedText2.count(jj),"\tNome:", nn,"\tFrequenza assoluta:", AnalyzedText2.count(nn), "\n" 
#PROBABILITA' CONGIUNTA
   #POSITIVE
    probCongiunta1 = {}
    for elem in AggSosOrdinati1:
        bigram1 = elem[0]
        a1 = elem[0][0]
        probCondiz1 = elem[1]*1.0 / AnalyzedText1.count(a1)*1.0          #calcolo la probabilità condizionata, richiesta nella formula della probabilità congiunta
        probA1 = AnalyzedText1.count(a1)*1.0 / len(TokenizedText1)*1.0   #calcolo la probabilità di A (prima parola del bigramma, ovvero l'aggettivo)
        probCong1 = probA1 * probCondiz1                                 #calcolo la probabilità congiunta
        probCongiunta1[bigram1] = probCong1                              #creo un nuovo elemento nel dizionario con il bigramma e la probabilità congiunta
    probCongOrdinata1 = list(ordina(probCongiunta1))
    print "Per probabilità congiunta massima:\nPOSITIVE:\n"
    for elem in probCongOrdinata1[0:20]:
        print "Bigramma:\t", elem[0], "\nProbabilità congiunta:\t", elem[1], "\n"
   #NEGATIVE
    probCongiunta2 = {}
    for elem in AggSosOrdinati2:
        bigram2 = elem[0]
        a2 = elem[0][0]
        probCondiz2 = elem[1]*1.0 / AnalyzedText2.count(a2)*1.0         
        probA2 = AnalyzedText2.count(a2)*1.0 / len(TokenizedText2)*1.0  
        probCong2 = probA2 * probCondiz2
        probCongiunta2[bigram2] = probCong2                               
    probCongOrdinata2 = list(ordina(probCongiunta2))
    print "\nNEGATIVE:\n"
    for elem in probCongOrdinata2[0:20]:
        print "Bigramma:\t", elem[0], "\nProbabilità congiunta:\t", elem[1], "\n"
#FORZA ASSOCIATIVA (LOCAL MUTUAL INFORMATION)
    #FORMULA LMI: log2(f(a,b)xC/f(a)xf(b))
   #POSITIVE
    MutualInformation1 = {}
    for elem in AggSosOrdinati1:
         bigram1 = elem[0]
         fxc1 = elem[1] * len(TokenizedText1)        #calcolo il primo elemento della formula: il prodotto tra la frequenza del bigramma e il totale di elementi nel corpus
         A1 = elem[0][0]                     
         B1 = elem[0][1]
         fA1 = AnalyzedText1.count(A1)              #calcolo la frequenza della prima parola del bigramma (l'aggettivo)
         fB1 = AnalyzedText1.count(B1)              #calcolo la frequenza della seconda parola del bigramma (il nome)
         fxf1 = fA1 * fB1                            #calcolo il secondo elemento della formula: il prodotto tra le frequenze delle singole parole
         LMI1 = elem[1]*(math.log((fxc1*1.0/fxf1*1.0),2))       #calcolo la Local Mutual Information
         MutualInformation1[bigram1] = LMI1            #creo un nuovo elemento nel dizionario con il bigramma e la LMI
    LocMutInfo1 = list(ordina(MutualInformation1))
    print "Per forza associativa (attraverso la LMI):\nPOSITIVE:\n"
    for elem in LocMutInfo1[0:20]:
        print "Bigramma:\t", elem[0], "\nLocal Mutual Information:\t", elem[1], "\n"
   #NEGATIVE
    MutualInformation2 = {}
    for elem in AggSosOrdinati2:
         bigram2 = elem[0]
         fxc2 = elem[1] * len(TokenizedText2)       
         A2 = elem[0][0]                     
         B2 = elem[0][1]
         fA2 = AnalyzedText2.count(A2)              
         fB2 = AnalyzedText2.count(B2)             
         fxf2 = fA2 * fB2                           
         LMI2 = elem[1]*(math.log((fxc2*1.0/fxf2*1.0),2))       
         MutualInformation2[bigram2] = LMI2           
    LocMutInfo2 = list(ordina(MutualInformation2))
    print "\nNEGATIVE:\n"
    for elem in LocMutInfo2[0:20]:
        print "Bigramma:\t", elem[0], "\nLocal Mutual Information:\t", elem[1], "\n"
#CATENE DI MARKOV (ORDINE 0, 1)
   #POSITIVE
    lencorpus1 = len(TokenizedText1)    #lunghezza del corpus
    FrequenzaToken1 = nltk.FreqDist(TokenizedText1)  #frequenza di tutti i token del testo
    probMax1 = 0.0        #probabilità massima per Markov di ordine 0   
    probMax11= 0.0        #probabilità massima per Markov di ordine 1
    listafrasitokenizzate1 = []
    for frase in frasi1:
        frase = frase.encode('utf-8')
        frasetokenizzata = nltk.word_tokenize(frase)
        if all(FrequenzaToken1[token] >2 for token in frasetokenizzata):   #tutti i token nella frase devono avere frequenza > 2
            listafrasitokenizzate1.append(frasetokenizzata)
    for frase in listafrasitokenizzate1:
        lenfrase = len(frase)
        if ((lenfrase>5) and (lenfrase<8)):         #la frase deve contenere tra i 6 e gli 8 token
            probabilita1, probtoken1 = Markov0(lencorpus1, FrequenzaToken1, frase)   #funzione che calcola la catena di Markov di ordine 0 (probabilità di eventi indipendenti)
            probDipendente1 = Markov1(TokenizedText1, FrequenzaToken1, frase)        #funzione che calcola la catena di Markov di ordine 1 (eventi dipendenti: usa la probabilità condizionata)
            if probabilita1 > probMax1: #assegnamento della probabilità massima nella catena di ordine 0
                probMax1 = probabilita1          #probabilità massima riscontrata
                fraseMax1 = frase                #frase con probabilità massima
                probtokenMax1 = probtoken1       #probabilità dei singoli token nella frase
            if probDipendente1 > probMax11:   #assegnamento della probabilità massima nella catena di ordine 1
                probMax11 = probDipendente1   #probabilità massima riscontrata
                fraseMax11 = frase            #frase con probabilità massima
    print "\n\tProbabilità di frasi calcolata con le catene di Markov:"
    print "\nPOSITIVE:\nFrase con probabilità massima con catena di Markov di ordine 0:\t", fraseMax1, "\tProbabilità:\t", probMax1
    for token in fraseMax1:
        print token, "\tProbabilità token:\t", probtokenMax1[token]    #stampo le probabilità dei singoli token della frase
    print "Frase con probabilità massima con catena di Markov di ordine 1:\t", fraseMax11, "\tProbabilità:\t", probMax11, "\n"
   #NEGATIVE
    lencorpus2 = len(TokenizedText2)
    FrequenzaToken2 = nltk.FreqDist(TokenizedText2)
    probMax2 = 0.0
    probMax21 = 0.0
    listafrasitokenizzate2 = []
    for frase in frasi2:
        frase = frase.encode('utf-8')
        frasetokenizzata = nltk.word_tokenize(frase)
        if all(FrequenzaToken2[token] >2 for token in frasetokenizzata):
            listafrasitokenizzate2.append(frasetokenizzata)
    for frase in listafrasitokenizzate2:
        lenfrase = len(frase)
        if ((lenfrase>5) and (lenfrase<8)):
            probabilita2, probtoken2 = Markov0(lencorpus2, FrequenzaToken2, frase)
            probDipendente2 = Markov1(TokenizedText2, FrequenzaToken2, frase)
            if probabilita2 > probMax2:
                probMax2 = probabilita2
                fraseMax2 = frase
                probtokenMax2 = probtoken2
            if probDipendente2 > probMax21:
                probMax21 = probDipendente2
                fraseMax21 = frase  
    print "\nNEGATIVE:\nFrase con la probabilità massima con catena di Markov di ordine 0:\t", fraseMax2, "\tProbabilità:\t", probMax2
    for token in fraseMax2:
        print token, "\tProbabilità:\t", probtokenMax2[token]
    print "\nFrase con probabilità massima con catena di Markov di ordine 1:\t", fraseMax21, "\tProbabilità:\t", probMax21, "\n"    


        
   
main(sys.argv[1],sys.argv[2])
