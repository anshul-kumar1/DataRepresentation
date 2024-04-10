import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.fft import fft2, ifft2, fftshift, ifftshift
from scipy.stats import stats
from skimage.color import rgb2gray
import scipy.fftpack

# Question 1
def dot_product(v1, v2):
    product = np.dot(v1, v2)
    magnitude = np.abs(product)
    real = np.real(product)
    imaginary = np.imag(product)
    phase_angle = np.angle(product)

    return product, magnitude, real, imaginary, phase_angle

print(dot_product(1 - 4j, 1 + 1j))
print(dot_product(5 - 4j, 3 + 0j))
print(dot_product(5 + 3j, 5 + 3j))
print(dot_product(5 + 3j, 5 - 3j))


# Question 2 #
# Implement the Discrete Time Fourier Transform (DTFT) algorithm which returns the coefficients of the DTFT of a signal.
def dtft_algorithm(signal, time):
    L = len(time)  # Length of the signal
    ft = np.arange(L) / L
    coeff = np.zeros((len(signal)), dtype=complex)

    for fi in range(L):
        csw = np.exp(-1j * 2 * np.pi * fi * ft)
        coeff[fi] = np.sum(np.multiply(signal, csw)) / L

    return coeff

srt = 1000
t = np.arange(0, 2.0, 1.0 / srt)
sgnl1 = 6 * np.sin(2 * np.pi * 3 * t) + 3 * np.sin(2 * np.pi * 6 * t)
coefficients1 = dtft_algorithm(sgnl1, t)
freq1 = np.arange(len(sgnl1)) * srt / len(sgnl1)

sgnl2 = np.sin(2 * np.pi * 3 * t) + np.cos(2 * np.pi * 6 * t)
coefficients2 = dtft_algorithm(sgnl2, t)
freq2 = np.arange(len(sgnl2)) * srt / len(sgnl2)

plt.figure(figsize=(10, 4))
plt.plot(freq1, np.abs(coefficients1))
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.xlim(0, 10)
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(freq2, np.abs(coefficients2))
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.xlim(0, 10)
plt.show()

# Question 3 #
# Reconstruction of the image using the Fourier Transform and removing high frequencies
astronaut_img = mpimg.imread("astronaut.png")
astronaut_img = np.mean(astronaut_img, axis=2)

if len(astronaut_img.shape) == 3:
    astronaut_img = rgb2gray(astronaut_img)

shifted = fftshift(fft2(astronaut_img))
amplitude = np.abs(shifted)
phase_an = np.angle(shifted)

f_recons = ifftshift(shifted)
rec = np.real(ifft2(f_recons))
error = np.mean(np.abs(astronaut_img - rec))

print(f"Mean Absolute Error:", error)
print(f"Amplitude:", amplitude)
print(f"Phase Angle:", phase_an)

# getting the co-ordinates of the center of the shifted image
a, b = shifted.shape
center_coordinates = (a//2, b//2)

# calculating the distance of each pixel from the center
dist_X, dist_Y = np.ogrid[:a, :b]

# implementing the distance formula (pythagorean theorem)
dist = np.sqrt((dist_X - center_coordinates[1]) ** 2 + (dist_Y - center_coordinates[0]) ** 2)
threshold = min(a, b) / 4
print("Threshold:", threshold)
# removing high frequencies
removed_high_freq = np.where(dist > threshold, 0, shifted)

# reconstructing the image with removed high frequencies
image_without_high_freq = np.real(ifft2(ifftshift(removed_high_freq)))

# Question 4 #
width = 0.1
meshx = np.linspace(-2, 2, astronaut_img.shape[0])
Y, X = np.meshgrid(meshx, meshx)  # at the center of the image

gauss2d = np.exp(- (X ** 2 + Y ** 2) / (2 * width ** 2))

# computing the fourier transform of the image
imgX = np.fft.fftshift(np.fft.fft2(astronaut_img))
img_filtered = np.real(np.fft.ifft2(np.fft.fftshift(imgX*gauss2d)))

plt.imshow(astronaut_img, cmap='gray')
plt.title('Original Reconstructed Image')
plt.axis('off')
plt.show()

plt.imshow(image_without_high_freq, cmap='gray')
plt.title('Reconstructed Image with High Frequencies Removed, Question 3')
plt.axis('off')
plt.show()

plt.imshow(img_filtered, cmap='gray')
plt.title('Gaussian filtering, Question 4')
plt.axis('off')
plt.show()