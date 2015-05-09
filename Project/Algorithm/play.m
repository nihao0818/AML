load('clicks5')
train_x = X(:,1:end-1);

train_x = double(train_x) ./ max(max(train_x,[],1),[],2);

% load mnist_uint8;
% 
% train_x = double(train_x)/255;
% test_x  = double(test_x)/255;
% train_y = double(train_y);
% test_y  = double(test_y);

%%  
% Setup and train a stacked denoising autoencoder (SDAE)
% rand('state',0)
% sae = saesetup([1000 100]);
% sae.ae{1}.activation_function       = 'sigm';
% sae.ae{1}.learningRate              = 1;
% sae.ae{1}.inputZeroMaskedFraction   = 0.5;
% opts.numepochs =   1;
% opts.batchsize = 100;
% sae = saetrain(sae, train_x, opts);
% % visualize(sae.ae{1}.W{1}(:,2:end)')
% 
% nn = sae.ae{1};
% x = train_x;
% 
%     n = nn.n;
%     m = size(x, 1);
%     
%     x = [ones(m,1) x];
%     nn.a{1} = x;
% 
%     %feedforward pass
%     for i = 2 : n-1
%         switch nn.activation_function 
%             case 'sigm'
%                 % Calculate the unit's outputs (including the bias term)
%                 nn.a{i} = sigm(nn.a{i - 1} * nn.W{i - 1}');
%             case 'tanh_opt'
%                 nn.a{i} = tanh_opt(nn.a{i - 1} * nn.W{i - 1}');
%         end
%         
%         %dropout
%         if(nn.dropoutFraction > 0)
%             if(nn.testing)
%                 nn.a{i} = nn.a{i}.*(1 - nn.dropoutFraction);
%             else
%                 nn.dropOutMask{i} = (rand(size(nn.a{i}))>nn.dropoutFraction);
%                 nn.a{i} = nn.a{i}.*nn.dropOutMask{i};
%             end
%         end
%         
%         %calculate running exponential activations for use with sparsity
%         if(nn.nonSparsityPenalty>0)
%             nn.p{i} = 0.99 * nn.p{i} + 0.01 * mean(nn.a{i}, 1);
%         end
%         
%         %Add the bias term
%         nn.a{i} = [ones(m,1) nn.a{i}];
%     end
%     switch nn.output 
%         case 'sigm'
%             nn.a{n} = sigm(nn.a{n - 1} * nn.W{n - 1}');
%         case 'linear'
%             nn.a{n} = nn.a{n - 1} * nn.W{n - 1}';
%         case 'softmax'
%             nn.a{n} = nn.a{n - 1} * nn.W{n - 1}';
%             nn.a{n} = exp(bsxfun(@minus, nn.a{n}, max(nn.a{n},[],2)));
%             nn.a{n} = bsxfun(@rdivide, nn.a{n}, sum(nn.a{n}, 2)); 
%     end
% 
% X_sae_tf = nn.a{2}(:,2:end);
% save('X_sae_tf','X_sae_tf')
    

   %%  ex1 train a 100 hidden unit RBM and visualize its weights
rand('state',0)
dbn.sizes = [100];
opts.numepochs =   4;
opts.batchsize = 100;
opts.momentum  =   0;
opts.alpha     =   1;
dbn = dbnsetup(dbn, train_x, opts);
dbn = dbntrain(dbn, train_x, opts);
% figure; visualize(dbn.rbm{1}.W');   %  Visualize the RBM weights

X_rbm = rbmup(dbn.rbm{1}, train_x);

nn = dbnunfoldtonn(dbn);

x = train_x;

    n = nn.n;
    m = size(x, 1);
    
    x = [ones(m,1) x];
    nn.a{1} = x;

    %feedforward pass
    for i = 2 : n-1
        switch nn.activation_function 
            case 'sigm'
                % Calculate the unit's outputs (including the bias term)
                nn.a{i} = sigm(nn.a{i - 1} * nn.W{i - 1}');
            case 'tanh_opt'
                nn.a{i} = tanh_opt(nn.a{i - 1} * nn.W{i - 1}');
        end
        
        %dropout
        if(nn.dropoutFraction > 0)
            if(nn.testing)
                nn.a{i} = nn.a{i}.*(1 - nn.dropoutFraction);
            else
                nn.dropOutMask{i} = (rand(size(nn.a{i}))>nn.dropoutFraction);
                nn.a{i} = nn.a{i}.*nn.dropOutMask{i};
            end
        end
        
        %calculate running exponential activations for use with sparsity
        if(nn.nonSparsityPenalty>0)
            nn.p{i} = 0.99 * nn.p{i} + 0.01 * mean(nn.a{i}, 1);
        end
        
        %Add the bias term
        nn.a{i} = [ones(m,1) nn.a{i}];
    end
    switch nn.output 
        case 'sigm'
            nn.a{n} = sigm(nn.a{n - 1} * nn.W{n - 1}');
        case 'linear'
            nn.a{n} = nn.a{n - 1} * nn.W{n - 1}';
        case 'softmax'
            nn.a{n} = nn.a{n - 1} * nn.W{n - 1}';
            nn.a{n} = exp(bsxfun(@minus, nn.a{n}, max(nn.a{n},[],2)));
            nn.a{n} = bsxfun(@rdivide, nn.a{n}, sum(nn.a{n}, 2)); 
    end

X_rbm_tf = nn.a{2};
save('X_rbm_tf','X_rbm_tf')

%%

% [mappedX, mapping] = isomap(train_x, 100, 12);

% D=pdist(train_x);
% [Y, R, E] = Isomap(D, 'k',3); 
