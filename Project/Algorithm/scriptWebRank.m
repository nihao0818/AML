
% load feature matrix
D = dlmread('X.txt.sparse');
M = full(sparse(D(:, 1) + 1, D(:, 2) + 1, D(:, 3), 100000, 1000));

% tf-idf weighting of term counts
idf = log(size(M, 1) ./ max(sum(M > 0, 1), 1));
score = log(M + 1) .* repmat(idf, size(M, 1), 1);
X = score;
% X = [X, ones(size(X, 1), 1)];

% load predictions
Y = dlmread('Y.txt');

% % rebalance
% Y = 0.5 * (Y > 0);

% evaluation
for query =  1 : 10
  fprintf('Query %i\n', query);
  
  % regression
  w = (X' * X + eye(size(X, 2))) \ (X' * Y(:, query));
  [yp, ndx] = sort(X * w, 'descend');
  
  % top K predictions 
  K = 10;
  for k = 1 : K
    fprintf('%2i: %7i, yhat = %7.4f, y = %7.4f | ', ...
      k, ndx(k), yp(k), Y(ndx(k), query));
    if (mod(k, 2) == 0)
      fprintf('\n');
    end 
  end
  fprintf('\n');
end

save('clicks6', 'X', 'Y');
