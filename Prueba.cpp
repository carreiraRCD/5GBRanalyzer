#include <iostream>
#include <fstream>
#include <complex>
#include <vector>

int main() {
    const char* dir = "RF-3MHz.iq";
    std::ifstream inputFile(dir, std::ios::binary);

    if (!inputFile) {
        std::cerr << "Error al abrir el archivo de entrada." << std::endl;
        return 1;
    }

    inputFile.seekg(0, std::ios::end);
    std::streampos fileSize = inputFile.tellg();
    inputFile.seekg(0, std::ios::beg);

    std::vector<int16_t> mem(fileSize / sizeof(int16_t));
    inputFile.read(reinterpret_cast<char*>(mem.data()), fileSize);
    inputFile.close();

    std::vector<std::complex<float>> data(mem.size() / 2);
    for (size_t i = 0; i < mem.size(); i += 2) {
        data[i / 2] = std::complex<float>(static_cast<float>(mem[i]), static_cast<float>(mem[i + 1]));
    }

    size_t n = data.size();
    std::vector<std::complex<float>> B(n);
    for (size_t i = 0; i < n; ++i) {
        B[i] = data[i] * std::exp(std::complex<float>(0, (4500.0 / 7680000.0 * 2 * M_PI) * i));
    }

    std::vector<float> D(2 * n);
    for (size_t i = 0, w = 0; i < n; ++i) {
        D[w++] = std::real(B[i]);
        D[w++] = std::imag(B[i]);
    }

    const char* outputFile = "5G-3MHz-2.raw";
    std::ofstream outputFileStream(outputFile, std::ios::binary);
    
    if (!outputFileStream) {
        std::cerr << "Error al abrir el archivo de salida." << std::endl;
        return 1;
    }

    outputFileStream.write(reinterpret_cast<char*>(D.data()), 2 * n * sizeof(float));
    outputFileStream.close();

    std::cout << "Proceso completado exitosamente." << std::endl;

    return 0;
}
