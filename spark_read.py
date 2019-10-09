# https://nlp.johnsnowlabs.com/docs/en/annotators


from sparknlp.training import CoNLL
training_conll = CoNLL().readDataset(spark, "./src/main/resources/conll2003/eng.train")


# >>> training_conll
# DataFrame[text: string, document: array<struct<annotatorType:string,begin:int,end:int,result:string,metadata:map<string,string>,embeddings:array<float>,sentence_embeddings:array<float>>>, sentence: array<struct<annotatorType:string,begin:int,end:int,result:string,metadata:map<string,string>,embeddings:array<float>,sentence_embeddings:array<float>>>, token: array<struct<annotatorType:string,begin:int,end:int,result:string,metadata:map<string,string>,embeddings:array<float>,sentence_embeddings:array<float>>>, pos: array<struct<annotatorType:string,begin:int,end:int,result:string,metadata:map<string,string>,embeddings:array<float>,sentence_embeddings:array<float>>>, label: array<struct<annotatorType:string,begin:int,end:int,result:string,metadata:map<string,string>,embeddings:array<float>,sentence_embeddings:array<float>>>]