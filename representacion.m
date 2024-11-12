% Mostrar representacion 

nexttile
plot(real(nssstime327))
title("NSSS SRSRan")

nexttile
plot(real(ds2))
title("NSSS Matlab")

nexttile
plot(abs(fft(nssstime327(1,10:137))))
title("Simbolo NSSS SRSRan")

nexttile 
plot(fftshift(abs(fft(ds2(10:137,1)))))
title("Simbolo NSSS Matlab")