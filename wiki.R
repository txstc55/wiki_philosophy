setwd("/Users/Tim/Desktop/R Project")

library(tm)
library(wordcloud)
library(RColorBrewer)
q<-read.csv("result.csv",header=FALSE)


jeopCorpus <- Corpus(VectorSource(q))
jeopCorpus <- tm_map(jeopCorpus, removePunctuation)

pal <- brewer.pal(12, "Paired")
pal1<- brewer.pal(12,"Set3")
pal2<- brewer.pal(8,"Accent")
pal3<- brewer.pal(8,"Dark2")
pal4<- brewer.pal(8,"Pastel2")
wordcloud(jeopCorpus, max.words = 200, random.color = FALSE,random.order = FALSE,colors=cbind(pal,pal1,pal2,pal4,pal3))

  
library(igraph)



library(network)
library(maps)
p<-read.csv('path_analysis.csv',header=FALSE)
q<-matrix(0,nrow=nrow(p),ncol=2)

for (i in c(1:nrow(p))){
  q[i,1]<-toString(p[i,1])
  q[i,2]<-toString(p[i,2])
}
 
g1<-graph(q)

plot.igraph(g1,,vertex.size=5,vertex.color=cbind(pal,pal1,pal2,pal4,pal3),edge.arrow.size=0)
