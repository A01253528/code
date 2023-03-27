% mod = py.importlib.import_module('test');
% py.importlib.reload(mod);
% 
% py.test.hello("Hola desde matlab")
%pe = pyenv;
%pe.Version
% i=0;
% t = tcpclient('localhost', 51001);
% while i < 3
%     if t.NumBytesAvailable > 0
%         output = read(t);
%         data = char(output(1:4));
%         pwrcmd = str2double(data)
%         i = i+1;
%     end
% end
% clear t;
% connect to the server
% t = tcpclient('localhost', 50007);
% fopen(t);
% 
% % write a message
% fwrite(t, 'This is a test message.'); 
% % read the echo
% bytes = fread(t, 
% [1, t.BytesAvailable]);
% char(bytes
% )
while 1
    t = tcpclient('localhost',50007 );
    output = read(t);
    datat=char(output)
    pwrcmd = str2double(datat);
    fprintf(pwrcmd);
    clear t;
    pause(10)
end