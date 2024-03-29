import numpy as np
import os
os.system("cls")

'''
Ao programar machine learning é necessario ter uma lista onde o numero de elementos é igual ao numero de entradas e o valor desse elemento representa o numero de neurons de cada camada

atributos das classe MLP:
NUM_INPUTS = numero de neuros de entrada
NUM_HIDDEN = numero de neuros de cada layer oculto
NUM_OUTPUTS = numero de neuros de saida

LAYERS = lista com o numero de neuros de cada layer

WEIGHTS = lista com as matrizes de pesos de cada layer
apresentar todos os atributos da classe MLP:

!! ativar os self.layers na classe !!

MLP= MLP()
print('total de pesos: ',len(MLP.weights))
print('total de camadas: ',len(MLP.layers))
print('numero de neuros de entrada: ',MLP.layers[0])
print('pesos da camada de entrada:\n',MLP.weights[0])
print('numero de neuros da 2 camada oculta:',MLP.layers[1])
print('pesos da 2 camada oculta:\n ',MLP.weights[1])
print('numero de neuros da 3 camada oculta:',MLP.layers[2])
print('pesos da 3 camada oculta: ',MLP.weights[2])
print('numero de neuros de saida: ',MLP.layers[-1])

'''

class MLP(): # criar uma classe de multi layer preception
    #criar uma função de inicialização(construtor) onde vai receber os parametros de entrada, saida e oculta    
    def __init__(self, num_inputs=3, num_hidden=[3,5], num_outputs=2): #os parametros default estão definidos como 3 neuros de entrada, 3 neuros de saida e 2 layers escondidos com 3 neuros cada
        #criar os atributos da classe
        self.num_inputs = num_inputs #numero de neuros de entrada default = 3
        self.num_hidden = num_hidden #numero de neuros de cada layer oculto default = [3,5] (2 layers com 3 e 5 neuros)
        self.num_outputs = num_outputs #numero de neuros de saida default = 2
        
        #criar os layers (vai concatenar os layers de entrada, ocultos e saida)
        layers = [self.num_inputs] + self.num_hidden + [self.num_outputs] #esta variavel é uma lista com o numero de neuros de cada layer, cada layer é um elemento da lista e o numero de neuros é o valor do elemento
     
        # self.layers = layers #adicionar a lista de layers na variavel layers da classe MLP


        weights = [] #criar uma lista de pesos
        for i in range(len(layers)-1): #criar um loop para criar os pesos de cada layer o range vai de 0 até o tamanho da lista layers -1 (o -1 é para não pegar o ultimo elemento da lista)
            weights.append(np.random.rand(layers[i], layers[i+1])) #criar uma matriz de pesos aleatorios #adicionar a matriz de pesos na lista de pesos
        self.weights = weights #adicionar a lista de pesos na variavel weights da classe MLP
        
          
          
        #criar uma lista com as ativações de cada layer
        activations = [] #criar uma lista vazia
        for i in range(len(layers)):
            activations.append(np.zeros(layers[i])) #vai criar uma matriz de zeros com o numero de neuros de cada layer numa variavel local
            self.activations = activations  #vai definir a lista de ativações como uma variavel da classe MLP
        
        
        #criar uma lista com as derivadas de cada layer
        derivatives = [] #criar uma lista vazia
        for i in range(len(layers)-1):
            derivatives.append(np.zeros((layers[i], layers[i+1]))) #vai criar uma matriz de zeros com o numero de neuros de cada layer numa variavel local
            self.derivates = derivatives # vai definir a lista de derivadas como uma variavel da classe MLP
        
         
       
    #criar uma função para ativar os resultados da multiplicação da matriz de ativação com a matriz de pesos
    def _sigmoid(self, x): #criar uma função para ativar os neuros
        return 1 / (1 + np.exp(-x)) #vai retornar o valor da função sigmoid   

    def _sigmoid_derivative(self, x): 
        return x * (1.0 - x)
    
    def _mse(self, target, output): #mid square error
        return np.average((target-output)**2)
          

    def foward_propagation(self, inputs):
        '''
        o primeiro a vai ser os inputs enquando os restantes vao ser as ativações
        a = s(h) resultado da ativação do valor de h(a multiplicação das matrizes)
        h = w * a resultado da multiplicação das matrizes de pesos com a matriz de ativação
        w = matriz de pesos
        
        '''        
        activations = inputs #criar uma variavel de ativação que vai receber os inputs para a primeira camada  
        
        self.activations[0] = activations #adicionar a ativação da primeira camada na lista de ativações    
          
        #c-> camada e w-> pesos
        for c, w in enumerate(self.weights): #criar um loop para percorrer a lista de pesos
            
            #calcular a ativação de cada layer
            #np.dor() esta funcção vai executar a multiplicação de 2 matrizes(pega na matriz de ativação(inputs na primera camada) e na matriz de pesos da respetiva camada)
            net_inputs = np.dot(activations, w) #calcular a ativação de cada layer
            
            #calcular a ativação de cada layer
            activations = self._sigmoid(net_inputs)#vai fazer a ativação de cada layer com a função sigmoid(pega nos resultados da multiplicação da matriz de ativação com a matriz de pesos) e vai ativar cada neuron com a função sigmoid
            self.activations[c+1] = activations # vai adicionar a ativação da camada na lista de ativações
        
            # a_3 = s(h_3) o resultado (ativação) vai ser o resultado da função sigmoid do a multiplicação da matriz de ativação com a matriz de pesos
        
            # h_3 = a_3*w_3 o resultado vai ser a multiplicação da matriz de ativação com a matriz de pesos
        
        return activations #vai devolver a ativação da ultima camada(os resultados da ultima camada) dependendo na quantidade de neuros de saida


    def back_propagate(self, error, verbose=False):
        for i in reversed(range(len(self.derivates))):
            activations = self.activations[i+1] 
            #na primeira execução o erro vai ser o passado na função
            #Quando o for chegar ao fim a variavel de erro vai ser o resultado da multiplicação do erro com a matriz de pesos
            delta = error * self._sigmoid_derivative(activations)   
            delta_reshape = delta.reshape(delta.shape[0],-1).T
            current_activations = self.activations[i]
            current_activations_reshaped = current_activations.reshape(current_activations.shape[0],-1) 
            self.derivates[i] = np.dot(current_activations_reshaped, delta_reshape)
            error=np.dot(delta, self.weights[i].T)    
            #é necessario fazer o reshape da matriz de ativação para que a multiplicação seja possivel
        
            if verbose:
                print('Derivatives for W{}: {}'.format(i, self.derivates[i]))

        return error    
            
    
    def gradient_descent(self, learningRate=1):
        for i in range(len(self.weights)):
            weights = self.weights[i]
            # print(f'original weights of w_{i}: ', weights)
            derivatives = self.derivates[i]
            weights += derivatives * learningRate
            # print(f'new weights of w_{i}: ', weights)
            
            
    def train(self, inputs, targets, epochs, learningRate):
        for i in range(epochs):
            sum_errors = 0
            for (input, target) in zip(inputs, targets):
                output = self.foward_propagation(input)
                error = target - output
                self.back_propagate(error)
                self.gradient_descent(learningRate)
                sum_errors += self._mse(target, output)
            print('Error: {} at epoch {}'.format(sum_errors/len(inputs), i))
            
        



if __name__ == "__main__":

    
    MLP= MLP(2, [5], 1)
    
    input = np.array([0.1, 0.2])
    
    target = np.array([0.3])
    
    output = MLP.foward_propagation(input)
    
    error = target - output
    
    MLP.back_propagate(error, verbose=True)
    
    MLP.gradient_descent(learningRate=1)
    





#criação de graifcos relacionados a audio

quit()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import soundfile as sf
import sounddevice as sd
from glob import glob
import librosa
import librosa.display
import os
from itertools import cycle
sns.set_theme(style="white", palette=None)
color_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"]
color_cycle = cycle(plt.rcParams["axes.prop_cycle"].by_key()["color"])

os.system("cls")

audios_files= glob("audios/*/*.wav")

def audio_info(audio_file, index=0):
    audio_infos , sr= librosa.load(audio_file[index]) #sr = sample rate
    
    print(pd.Series(audio_infos))
    print(f"Sample rate: {sr}")
    print(f"Duration: {len(audio_infos)/sr} seconds")
    print(f"Number of samples: {len(audio_infos)}")
    print(f"value of the first sample: {audio_infos[0]}")

    values=[]
    total=0
    for i in range(0, len(audio_infos)):
        print(f"index: {i} value: {audio_infos[i]}")
        total += audio_infos[i]
        if audio_infos[i] not in values:
            values.append(audio_infos[i])       
    
    print(pd.Series(values))
    print("min value: {:.6f}".format(np.min(audio_infos)))
    print("max value: {:.6f}".format(np.max(audio_infos)))
    print("mean value: {:.6f}".format(np.mean(audio_infos)))    

    pd.Series(audio_infos).plot()
    plt.show()   


 
audio_info(audios_files)

