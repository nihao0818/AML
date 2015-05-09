data = importdata('remappered.data');
[row,col] = size(data);
neg_data = data(data(:,7)==-1);
pos_data = data(data(:,7)==1);
[p_row,P_col] = size(pos_data);
[n_row,n_col] = size(neg_data);
neg_prior = p_row/row;
pos_prior = n_row/row;

