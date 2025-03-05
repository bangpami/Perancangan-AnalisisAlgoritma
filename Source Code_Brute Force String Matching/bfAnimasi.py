import matplotlib.pyplot as plt
import time

def visualize_brute_force_string_match(T, P):
    n = len(T)
    m = len(P)
    
    fig, ax = plt.subplots()
    
    for i in range(n - m + 1):
        j = 0
        match = True
        while j < m and P[j] == T[i + j]: 
            j += 1
        
        if j != m:  
            match = False

        
        ax.clear()
        text_display = " ".join(T)
        pattern_display = " " * (2 * i) + " ".join(P)  
        
        ax.text(0.1, 0.6, "Teks:    " + text_display, fontsize=16, family="monospace")
        ax.text(0.1, 0.4, "Pola:    " + pattern_display, fontsize=16, family="monospace", color="red" if not match else "green")
        
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")

        plt.pause(2)  
    
    plt.show()


text = "RamdhanBulanBerkah"
pattern = "Bulan"
visualize_brute_force_string_match(text, pattern)
