
% load data
load('X_rbm_tf');
% 
X = X_rbm_tf;
% Y = dlmread('Y.txt');
% load('clicks5');
Y = dlmread('Y.txt');
% feature selection
% X = X(:, 101 : 200);
% X = X(:, 1:end-1);
% [C,X,L] = pca(X,'NumComponents',100);

% X = dlmread('output.txt');

X = [X, ones(size(X, 1), 1)];
numFeatures = size(X, 2);


% parameters
K = 10;
lambda = 1;
numExps = 3;
T = 2000;

% evaluation
for query =  1 : 10
  numStates = 1000;
  y = Y(:, query);
  W = double(rand(numStates, length(y)) < repmat(y', numStates, 1));
  
  % simulation
  reward = zeros(T, numExps);
  
  for ex = 1 : numExps
    % Gaussian prior
    gram = lambda * eye(numFeatures);
    Xty = zeros(numFeatures, 1);
    mu = zeros(numFeatures, 1);
    
    states = ceil(rand(1, T) * numStates);
    for t = 1 : T
      wt = W(states(t), :);
      
      % recommend K items
      thetat = mvnrnd(mu', gram)';
      what = (X * thetat)';
      [~, At] = sort(what, 'descend');
      At = At(1 : K);
      reward(t, ex) = any(wt(At) > 0);
      
      % posterior update based on examined items
      click = find(wt(At) == 1, 1, 'first');
      if (isempty(click))
        obs = At;
      else
        obs = At(1 : click);
      end
      for e = obs
        gram = gram + X(e, :)' * X(e, :);
        Xty = Xty + X(e, :)' * wt(e);
      end
      mu = gram \ Xty;
      
      if (mod(t, 100) == 0)
        fprintf('.');
      end
    end
    fprintf(' ');
    
    rewardT = mean(reward(:, 1 : ex), 1);
    fprintf('%.2f \\pm %.2f\n', mean(rewardT), std(rewardT) / sqrt(ex));
  end
  fprintf('\n');
  
  val = mean(reshape(mean(reward, 2), T / 10, 10), 1);
  times = round((1 : 10) * T / 10);
  
  fprintf('Query %i\n', query);
  fprintf('%s\n', sprintf('%4i ', times));
  fprintf('%s\n\n', sprintf('%.2f ', val));
end
