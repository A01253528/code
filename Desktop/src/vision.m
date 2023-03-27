clc;
clear;

cam = webcam(2);
wb = waitbar(0,"Name","Espera...",'CreateCancelBtn','delete(gcbf)');
i=0;

while true
    img0 = snapshot(cam);
    img=imsubstract(img0(:,:,3),rgb2gray(img0));
    imshow(img0);

    if ~ishandle(wb)
        break
    else 
        eaitbar(i/10,wb,['num: ' num2str(i)]);
    end

    i = i+1;
    pause(0.001);
end
clear cam;