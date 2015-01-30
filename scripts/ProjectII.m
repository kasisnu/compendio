I = imread('C:\Users\Pronoy\Pictures\project\OCRExample_06.jpg');
M = csvread('C:\Users\Pronoy\Pictures\project\ph.dat');
red = uint8([255 0 0]);
markerStart = vision.MarkerInserter('Shape','Plus','BorderColor','Custom','CustomBorderColor',red);
startPts = int32([M(:,1) M(:,2)]);
J = step(markerStart, I, startPts);
endPts = int32([M(:,3) M(:,4)]);
J = step(vision.MarkerInserter('BorderColor','Custom','CustomBorderColor',red), J, endPts);
figure, imshow(J);
Iheight = imtophat(imcrop(imcomplement(I),[0 int32(0.2*size(I,1))  size(I,2) int32(0.6*size(I,1))]),strel('disk',15));
results = ocr(Iheight);
textHeight = int32(1.5*mean(results.WordBoundingBoxes(:,4)));
for k = 1:size(M,1)
    xOpen=M(k,1); yOpen=M(k,2);
    xClose=M(k,3); yClose=M(k,4);
    shapeInserter = vision.ShapeInserter('Fill',1,'FillColor','Black','Opacity',1);
    rectangles = int32([0 yOpen xOpen textHeight;xClose (yClose-textHeight-3) (size(I,2)-xClose) (textHeight+3)]);
    Irect = step(shapeInserter,imcomplement(I),rectangles);
    Icrop = imtophat(imcrop(Irect,[0 yOpen size(I,2) (yClose-yOpen)]),strel('disk',15));
    figure, imshow(imcomplement(Icrop));
    results = ocr(Icrop);
    fprintf('\nSelection #%d :',k);
    results.Text
end