%Lectura de ficheiros de texto

dir = 'TFG/RF.iq'

fid = fopen(dir, 'r');
mem = fread(fid,100); % ,'ieee-le'


fclose(fid);


