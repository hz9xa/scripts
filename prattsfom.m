function fom = FOM(orig,filted)
% Calculate Pratt's figure of merit to measure edge preservation
% performance of a filter
% 
% In the response of an edge detector,there can be three types of errors:
% 1. Missing valid edges
% 2. Errors in localizing edges
% 3. Classification of noise as edges
% Pratt's figure of merit consider these three errors.

ide = edge(orig,'canny',[],1);
det = edge(filted,'canny',[],1);

MAXedge = max(length(find(ide)),length(find(det)));

[Rdet, Cdet] = find(det);
[Ride, Cide] = find(ide);
d = sqrt(size(ide,1)^2+size(ide,2)^2)*ones(1,length(find(ide)));
dd = zeros(1,length(find(det)));

for i = 1:length(find(det))
    for j = 1:length(find(ide))
        d(j) = (Rdet(i)-Ride(j))^2+(Cdet(i)-Cide(j))^2;
    end
    dd(i) = min(d);
end

fom = sum(9./(9+dd))/MAXedge;

