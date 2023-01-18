import tkinter as tk
from tkinter import filedialog
import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np

# creeaza fereastra
window = tk.Tk()
window.title('Prelucrarea semnalelor audio')

#determina dimensiunile ecranului
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#seteaza dimensiunile si pozitionarea ferestrei astfel incat sa fie centrata pe ecran
window.geometry(f'500x300+{screen_width//2 - 250}+{screen_height//2 - 150}')

def path_audio():
    # specificam ca variabila este globala
    global selected_filepath  
    # deschide dialogul de alegere a fisierului
    selected_filepath = filedialog.askopenfilename()
    # afiseaza calea fisierului ales
    print(selected_filepath)
    label = tk.Label(window, text=selected_filepath)
    label.pack()

# functie apelata cand este apasat butonul grafic inainte de aplicare DFT
def display_graph():
    # deschide fisierul audio
    data, samplerate = sf.read(selected_filepath, dtype='int16')
    # converteste datele intr-un array numpy
    data = np.array(data)
    # afiseaza  graficul semnalului audio
    plt.plot(data)
    plt.show()

# functie apelata cand este apasat butonul Afisare Grafic Audio Comparativ 
def display_graph_DFT():
    #deschide fisierul audio
    data, samplerate = sf.read(selected_filepath, dtype='int16')
    #converteste datele intr-un array numpy
    data = np.array(data)
    # aplicarea DFT asupra datelor semnalului audio
    fourier_transform = np.fft.fft(data)

    #comprimare
    # eliminarea componentelor de frecventa care nu sunt retinute
    N = 3000  # numarul de componente de frecventa care sunt retinute
    fourier_transform[N:] = 0
    # calcularea inversului DFT pentru a reconstrui semnalul comprimat
    compressed_data = np.fft.ifft(fourier_transform)

    # păstrați partea complexă a datelor prin convertirea la tipul de date 'float32'
    f_compressed_data = compressed_data.astype('float32')
    # specificați calea către noul fișier audio
    new_filepath = 'compressed_audio.wav'
    # scrieți semnalul comprimat în noul fișier audio
    sf.write(new_filepath, f_compressed_data, samplerate)

    # afisarea semnalului original pe axa X
    plt.plot(data, color='#08689c', label='semnal original')
    # afisarea semnalului comprimat pe aceeasi axa X
    plt.plot(compressed_data, color='red', label='semnal comprimat')
    plt.show()


# creeaza butonul0 pentru alegerea fisierului audio
button0 = tk.Button(window, text='Alege fisier Audio', command=path_audio)
# creeaza butonul1 pentru afisarea grafica a semnalului original audio
button1 = tk.Button(window, text='Afisare Grafic Audio Original', command=display_graph)
# creeaza butonul2 pentru afisarea grafica a comparatiei dintre semnalul audio original si cel comprimat
button2 = tk.Button(window, text='Afisare Grafic Audio Comparativ', command=display_graph_DFT)

#setarea pozitiei butoanelor
button0.pack(pady=10)
button1.pack(pady=10)
button2.pack(pady=10)

# ruleaza aplicatia
window.mainloop()
