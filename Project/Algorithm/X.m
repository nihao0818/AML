% load data matrix
D = dlmread('X.txt');
M = full(sparse(D(:, 1) + 1, D(:, 2) + 1, D(:, 3), 100000, 1000));

% % features are 100 most frequent terms
% topTerms = 1000;
% [val, ndx] = sort(M, 2, 'descend');
% X = double(full(sparse(...
%   repmat((1 : size(M, 1))', 1, topTerms), ...
%   ndx(:, 1 : topTerms), val(:, 1 : topTerms) > 0, ...
%   size(M, 1), size(M, 2))));
% 
% % load predictions
% Y = dlmread('Y.txt');
% 
% % rebalance
% Y = 0.5 * (Y > 0);

% X = X(1:100,:);
% X = M(1:100,:);
X = M;


% % tf-idf weighting of term counts
% idf = log(size(M, 1) ./ max(sum(M > 0, 1), 1));
% score = log(M + 1) .* repmat(idf, size(M, 1), 1);
% X = score;
% X = [X, ones(size(X, 1), 1)];

% M = [1:10;11:20;31:40];
% [coeff,score,latent] = pca(M,'NumComponents',3);
% 
% hh = score*coeff'

dlmwrite('/Users/haoni/Documents/Advanced Machine Learning/Project/Final/X_full_freq.txt',X,'precision','%.0f');