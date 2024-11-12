%Lectura de ficheros

dir = 'RF-3MHz.iq';

fid = fopen(dir, 'r');
% mem =fread(fid, 'double');
mem = fread(fid,'int16=>float32'); % ,'ieee-le'

data = mem(1:2:end-1)+1j*mem(2:2:end);
fclose(fid); 
% 
n=1:length(data);
B = data.*exp(1j*(4500/7680000*2*pi)*n');

% mem = resample(mem, 76300, 78125);

w=1;
        for i = 1:length(B)

            D(w,1)=real(B(i,1));
            D(w+1,1)=imag(B(i,1));
            w = w+2;
        end

file = fopen('5G-3MHz.raw','w');
fwrite(file,D,'float32');
fclose(file);

