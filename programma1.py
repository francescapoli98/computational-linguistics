# -*- coding: utf-8 -*-
import sys
import codecs
import re
import nltk

#POS TAGGER 
def AnnotazioneLing(frasi):
    tokensTOT = []
    tokensPOStot = []
   #for per tokenizzare le frasi e poi analizzarle, e creare le liste di token e tag
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
       #inserire elementi in coda alla listaPOS
        listaPOS.append(bigramma[1])
    return listaPOS

#calcolo il numero di token nelle frasi dei corpora (=lunghezza del corpus)
def CalcolaLunghezzaFrase(frasi):
    numerotokens = []
    lunghezza = 0.0
    for frase in frasi:
        frase = frase.encode('utf-8')
        tokens = nltk.word_tokenize(frase)
        numerotokens = numerotokens + tokens
        lunghezza = len(numerotokens)
    return lunghezza

#calcolo il numero di caratteri di ogni token 
def CalcolaLunghezzaToken(frasi):
    numcaratteri = 0.0
    numtoken = []
    for frase in frasi:
        frase = frase.encode('utf-8')
        tokens = nltk.word_tokenize(frase)
        numtoken = numtoken + tokens
        for token in tokens:
            caratteri = len(token)
            numcaratteri = numcaratteri + caratteri
    return numcaratteri

#CALCOLO VOCABOLARIO E TTR PER PORZIONI INCREMENTALI
def CalcoloVT(testop):
   #prendo le word type della porzione di testo
    vocabolario = set(testop)
   #conto le word type
    voc = len(vocabolario)
   #corpus=numero token in analisi
    corpus = len(testop)
    TTR = voc*1.0/corpus*1.0
    return voc, TTR



def main(file1,file2):
    fileInput1=codecs.open(file1,'r','utf-8')
    raw1=fileInput1.read()
    fileInput2=codecs.open(file2,'r','utf-8')
    raw2=fileInput2.read()
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    frasi1=sent_tokenizer.tokenize(raw1)
    frasi2=sent_tokenizer.tokenize(raw2)
    #POS TAGGER
   #chiamo la funzione che fa il POS tagging
    TokenizedText1, AnalyzedText1 = AnnotazioneLing(frasi1)
    TokenizedText2, AnalyzedText2 = AnnotazioneLing(frasi2)
   #chiamo la funzione che crea la sequenza token-tag
    SequenzaPOS1 = EstraiSequenza(AnalyzedText1)
    SequenzaPOS2 = EstraiSequenza(AnalyzedText2)
#NUMERO FRASI E TOKEN NEI CORPORA
    print "\n\tNumero di frasi e token in ogni corpus:\n"
    print "POSITIVE:\nNumero di frasi:\t", len(frasi1), "\tNumero di token:\t", len(TokenizedText1), "\nNEGATIVE:\nNumero di frasi:\t", len(frasi2),  "\tNumero di token:\t", len(TokenizedText2), "\n"
    if (len(frasi1) > len(frasi2)):
          print "Il corpus Positive presenta un numero maggiore di frasi"
    if (len(frasi1) < len(frasi2)):
          print "Il corpus Negative presenta un numero maggiore di frasi"
    if (len(frasi1) == len(frasi2)):
          print "I due corpora presentano lo stesso numero di frasi"
#LUNGHEZZA MEDIA DI FRASI E TOKEN 
   #chiamo la funzione che conta il numero di token in una frase
    frasemedia1 = CalcolaLunghezzaFrase(frasi1)
    frasemedia2 = CalcolaLunghezzaFrase(frasi2)
   #calcolo i token medi per frase
    MediaF1 = frasemedia1*1.0/len(frasi1)*1.0
    MediaF2 = frasemedia2*1.0/len(frasi2)*1.0
   #chiamo la funzione che conta la lunghezza media dei token
    tokenmedio1 = CalcolaLunghezzaToken(frasi1)
    tokenmedio2 = CalcolaLunghezzaToken(frasi2)
   #calcolo i caratteri medi per token
    MediaT1 = tokenmedio1*1.0/frasemedia1*1.0
    MediaT2 = tokenmedio2*1.0/frasemedia2*1.0
    print "\n\tNumero medio di token per frase e di caratteri per token in ogni corpus:\n"
    print "\nPOSITIVE:\nNumero medio di token per frase:", MediaF1, "\tNumero medio di caratteri per token:", MediaT1, "\nNEGATIVE:\n", "Numero medio di token per frase:", MediaF2, "\tNumero medio di caratteri per token:", MediaT2, "\n"
    if (MediaF1 > MediaF2):
          print "Il corpus Positive ha un maggior numero medio di token per frase"
    if (MediaF1 < MediaF2):
          print "Il corpus Negative ha un maggior numero medio di token per frase"
    if (MediaF1 == MediaF2):
          print "I corpora presentano lo stesso numero medio di token per frase"
    if (MediaT1 > MediaT2):
          print "Il corpus Positive presenta un maggior numero medio di caratteri per token"
    if (MediaT1 < MediaT2):
          print "Il corpus Negative presenta un maggior numero medio di caratteri per token"
    if (MediaT1 == MediaT2):
          print "I due corpora presentano lo stesso numero medio di caratteri per token"
#NUMERO MEDIO DI SOSTANTIVI, AGGETTIVI E AVVERBI NEI CORPORA
   #POSITIVE
   #sostantivi
    Sostantivi1 = []
    for line in SequenzaPOS1:
        StringaNomi = re.findall(r'NN|NNP|NNS|NNPS', line)
        for nome in StringaNomi:
            Sostantivi1.append(StringaNomi)
    Sostantivi1 = len(Sostantivi1)
   #aggettivi
    Aggettivi1 = []
    for line in SequenzaPOS1:
        StringaAgg = re.findall('JJ|JJR|JJS', line)
        for agg in StringaAgg:
            Aggettivi1.append(StringaAgg)
    Aggettivi1 = len(Aggettivi1)
   #avverbi
    Avverbi1 = []
    for line in SequenzaPOS1:
        StringaAdv = re.findall(r'RB|RBR|RBS', line)
        for adv in StringaAdv:
            Avverbi1.append(StringaAdv)
    Avverbi1 = len(Avverbi1)
   #medie
    MediaSos1 = Sostantivi1*1.0/len(frasi1)*1.0
    MediaAgg1 = Aggettivi1*1.0/len(frasi1)*1.0
    MediaAdv1 = Avverbi1*1.0/len(frasi1)*1.0
   #NEGATIVE
   #sostantivi
    Sostantivi2 = []
    for line in SequenzaPOS2:
        StringaNomi = re.findall(r'NN|NNP|NNS|NNPS', line)
        for nome in StringaNomi:
            Sostantivi2.append(StringaNomi)
    Sostantivi2 = len(Sostantivi2)
   #aggettivi
    Aggettivi2 = []
    for line in SequenzaPOS2:
        StringaAgg = re.findall('JJ|JJR|JJS', line)
        for agg in StringaAgg:
            Aggettivi2.append(StringaAgg)
    Aggettivi2 = len(Aggettivi2)
   #avverbi
    Avverbi2 = []
    for line in SequenzaPOS2:
        StringaAdv = re.findall(r'RB|RBR|RBS', line)
        for adv in StringaAdv:
            Avverbi2.append(StringaAdv)
    Avverbi2 = len(Avverbi2)
   #medie
    MediaSos2 = Sostantivi2*1.0/len(frasi2)*1.0
    MediaAgg2 = Aggettivi2*1.0/len(frasi2)*1.0
    MediaAdv2 = Avverbi2*1.0/len(frasi2)*1.0
    print "\n\tNumero medio di sostantivi, aggettivi e avverbi in ogni corpus:\n"
    print "\nPOSITIVE:\n", "Media di sostantivi per frase:\t", MediaSos1, "\tMedia di aggettivi per frase:\t", MediaAgg1, "\tMedia di avverbi per frase:\t", MediaAdv1, "\nNEGATIVE:\n", "Media di sostantivi per frase:\t", MediaSos2, "\tMedia di aggettivi per frase:\t", MediaAgg2, "\tMedia di avverbi per frase:\t", MediaAdv2
#DENSITA' LESSICALE
   #POSITIVE
    sequenzapos1 = []
    SosAggAdv1 = Sostantivi1 + Aggettivi1 + Avverbi1   #sommo le parti del discorso che mi servono per calcolare la densità lessicale
    for elem in SequenzaPOS1:
        if (elem not in ['.',',']):
            sequenzapos1.append(elem)  #scorrendo la lista di elementi postaggati, elimino la punteggiatura
    DensLess1 = SosAggAdv1*1.0/len(sequenzapos1)*1.0    #calcolo la densità lessicale
   #NEGATIVE
    sequenzapos2 = []
    SosAggAdv2 = Sostantivi2 + Aggettivi2 + Avverbi2
    for elem in SequenzaPOS2:
        if (elem not in ['.',',']):
            sequenzapos2.append(elem) 
    DensLess2 = SosAggAdv2*1.0/len(sequenzapos2)*1.0
    print "\n\tDensità lessicale:\nPOSITIVE:\t", DensLess1, "\nNEGATIVE:\t", DensLess2, "\n"
   #calcolo quale corpus ha densità lessicale maggiore
    if DensLess1>DensLess2:
          print "Il corpus Positive ha una densità lessicale maggiore"
    if DensLess2>DensLess1:
          print "Il corpus Negative ha una densità lessicale maggiore"
    if DensLess1==DensLess2:
          print "I due corpora hanno la stessa densità lessicale"
#CALCOLO VOCABOLARIO E TTR PER PORZIONI INCREMENTALI DI 1000 TOKEN
   #POSITIVE
    print "\n\tVocabolario e TTR per porzioni incrementali:\nPOSITIVE:\n"
    parziale1 = TokenizedText1[0:1000] #NumeroTok: testo tokenizzato all'inizio del main per contare la lunghezza del corpus in token
    voc, TTR = CalcoloVT(parziale1) 
    print "Porzione di 1000 token: \nVocabolario:\t", voc, "\tTTR:\t", TTR, "\n"
    parziale2 = TokenizedText1[0:2000] #uso la funzione per liste L[m:n] che seleziona gli elementi da m a n
    voc, TTR = CalcoloVT(parziale2) #chiamo la funzione che calcola sia il vocabolario della porzione sia la TTR
    print "Porzione di 2000 token:\nVocabolario:\t", voc, "\tTTR:\t", TTR, "\n"
    parziale3 = TokenizedText1[0:3000]
    voc, TTR = CalcoloVT(parziale3)
    print "Porzione di 3000 token:\nVocabolario:\t", voc, "\tTTR:\t", TTR, "\n"
    parziale4 = TokenizedText1[0:4000]
    voc, TTR = CalcoloVT(parziale4)
    print "Porzione di 4000 token:\nVocabolario:\t", voc, "\tTTR:\t", TTR, "\n"
    parziale5 = TokenizedText1[0:5000]
    voc, TTR = CalcoloVT(parziale5)
    print "Porzione di 5000:\nVocabolario:\t", voc, "\tTTR:\t", TTR, "\n"
   #ultimo passaggio, in cui considero il testo nella sua interezza
    voc, TTR = CalcoloVT(TokenizedText1)
    print "Vocabolario del testo in totale:\t", voc, "\tTTR del testo in totale:\t", TTR, "\n"
   #NEGATIVE
    parziale10 = TokenizedText2[0:1000]
    voc, TTR = CalcoloVT(parziale10)
    print "NEGATIVE:\n", "Porzione di 1000 token:\nVocabolario:\t", voc, "\tTTR:\t", TTR, "\n"
    parziale20 = TokenizedText2[0:2000]
    voc, TTR = CalcoloVT(parziale20)
    print "Porzione di 2000 token:\nVocabolario:\t", voc, "\tTTR:", TTR, "\n"
    parziale30 = TokenizedText2[0:3000]
    voc, TTR = CalcoloVT(parziale30)
    print "Porzione di 3000 token:\nVocabolario:\t", voc, "\tTTR:\t", TTR, "\n"
    parziale40 = TokenizedText2[0:4000]
    voc, TTR = CalcoloVT(parziale40)
    print "Porzione di 4000 token:\nVocabolario:\t", voc, "\tTTR:\t", TTR, "\n"
    parziale50 = TokenizedText2[0:5000]
    voc, TTR = CalcoloVT(parziale50)
    print "Porzione di 5000 token:\nVocabolario:\t", voc, "\tTTR:\t", TTR, "\n"
   #ultimo passaggio, in cui considero il testo nella sua interezza
    voc, TTR = CalcoloVT(TokenizedText2)
    print "Vocabolario del testo in totale:\t", voc, "\tTTR del testo in totale:\t", TTR, "\n"
#CALCOLO CLASSI DI FREQUENZA V3, V6 E V9
    print "\n\tClassi di frequenza v3, v6 e v9 nei due corpora:\n"
    v3_1 = 0
    v6_1 = 0
    v9_1 = 0
    FrequenzaToken1 = nltk.FreqDist(TokenizedText1)
    vocabolario1 = set(FrequenzaToken1)
    for token in vocabolario1:
          if FrequenzaToken1[token] == 3:
                v3_1 = v3_1 + 1
          if FrequenzaToken1[token] == 6:
                v6_1 = v6_1 + 1
          if FrequenzaToken1[token] == 9:
                v9_1 = v9_1 + 1
    print "\nPOSITIVE:", "\n|V3|:\t", v3_1, "\t|V6|:\t", v6_1, "\t|V9|:\t", v9_1
    v3_2 = 0
    v6_2 = 0
    v9_2 = 0
    FrequenzaToken2 = nltk.FreqDist(TokenizedText2)
    vocabolario2 = set(FrequenzaToken2)
    for token in vocabolario2:
          if FrequenzaToken2[token] == 3:
                v3_2 = v3_2 + 1
          if FrequenzaToken2[token] == 6:
                v6_2 = v6_2 + 1
          if FrequenzaToken2[token] == 9:
                v9_2 = v9_2 + 1
    print "\nNEGATIVE:", "\n|V3|:\t", v3_2, "\t|V6|:\t", v6_2, "\t|V9|:\t", v9_2
    
main(sys.argv[1],sys.argv[2])
