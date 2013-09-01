function ssim_compare_folder( baseline_image, folder_name)

% Takes a baseline image as the first parameter.
% Takes the name of the folder to iterate through as the second parameter
% Results are printed to a file in the current directory called
% "ssim_<folder_name>.txt"

results_name = strcat('ssim_', folder_name, '.txt');
out_handle = fopen(results_name,'w');
base = imread(baseline_image);


fList = ls(folder_name);
end_of_contents = size(fList,1);

fprintf(out_handle, 'Comparison to %s:\n\n',baseline_image); 

for image = 1 : end_of_contents
    item = fList(image,:);

    not_an_image = regexp(item,'^\.\.?\s*', 'ONCE');
    if  ~ isempty(not_an_image)
        continue
    end
    
    img_name = deblank(item);
    cd(folder_name);
    cmp_img = imread(img_name);
    cd('..');
    ssim_val = ssim(base,cmp_img);
    
    fprintf(out_handle, '%s: %f\n', img_name, ssim_val);
end

fclose(out_handle);
return;