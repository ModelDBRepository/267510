

%%


clc
clear all
close all
%%
NN= 50  ;
%

filenames = {'data0.mat','data1.mat','data2.mat','data3.mat','data4.mat','data5.mat','data6.mat','data7.mat','data8.mat' ,'data9.mat'  ,'data10.mat' , 'data11.mat','data12.mat','data13.mat','data14.mat','data15.mat','data16.mat','data17.mat','data18.mat','data19.mat','data20.mat','data21.mat','data22.mat','data23.mat','data24.mat','data25.mat','data26.mat','data27.mat','data28.mat','data29.mat','data30.mat','data31.mat','data32.mat','data33.mat','data34.mat','data35.mat','data36.mat','data37.mat','data38.mat','data39.mat','data40.mat','data41.mat','data42.mat','data43.mat','data44.mat','data45.mat','data46.mat','data47.mat','data48.mat','data49.mat'};                                                                                            
for kk = 1:numel(filenames)
    load(filenames{kk})  ;% Best to load into an output variable.
   
end




%
t=0:0.01:1000*12 ;
t= round(t*100)/100  ;

Q = zeros(NN,length(t))  ;


%

for i=1:length(data0)
a = find (t==round(data0(1,i)*100)/100 )  ;
Q(1,a) =1  ;


end
% 
% 
% for i=1:length(data1)
% a = find (t==round(data1(1,i)*100)/100 )  ;
% Q(2,a) =1  ;
% 
% end

% 
% for i=1:length(data2)
% a = find (t== round(data2(1,i)*100)/100  )  ;
% Q(3,a) =1  ;
% 
% end
% 
% 
% for i=1:length(data3)
% a = find (t==round(data3(1,i)*100)/100 )  ;
% Q(4,a) =1  ;
% 
% end
% 
% for i=1:length(data4)
% a = find (t==round(data4(1,i)*100)/100 )  ;
% Q(5,a) =1  ;
% 
% end

% 
% 
% for i=1:length(data5)
% a = find (t==round(data5(1,i)*100)/100 )  ;
% Q(6,a) =1  ;
% 
% end
% 
% for i=1:length(data6)
% a = find (t==round(data6(1,i)*100)/100 )  ;
% Q(7,a) =1  ;
% 
% end
% 
% 
% for i=1:length(data7)
% a = find (t==round(data7(1,i)*100)/100 )  ;
% Q(8,a) =1  ;
% 
% end
% 
% for i=1:length(data8)
% a = find (t==round(data8(1,i)*100)/100 )  ;
% Q(9,a) =1  ;
% 
% end
% % 
% for i=1:length(data9)
% a = find (t==round(data9(1,i)*100)/100 )  ;
% Q(10,a) =1  ;
% 
% end

% for i=1:length(data10)
% a = find (t==round(data10(1,i)*100)/100 )  ;
% Q(11,a) =1  ;
% 
% end
% 
% for i=1:length(data11)
% a = find (t==round(data11(1,i)*100)/100 )  ;
% Q(12,a) =1  ;
% 
% end
% 
% for i=1:length(data12)
% a = find (t==round(data12(1,i)*100)/100 )  ;
% Q(13,a) =1  ;
% 
% end
% 
% for i=1:length(data13)
% a = find (t==round(data13(1,i)*100)/100 )  ;
% Q(14,a) =1  ;
% 
% end
% 
% for i=1:length(data14)
% a = find (t==round(data14(1,i)*100)/100 )  ;
% Q(15,a) =1  ;
% 
% end
% 
% for i=1:length(data15)
% a = find (t==round(data15(1,i)*100)/100 )  ;
% Q(16,a) =1  ;
% 
% end
% 
% for i=1:length(data16)
% a = find (t==round(data16(1,i)*100)/100 )  ;
% Q(17,a) =1  ;
% 
% end
% 
% for i=1:length(data17)
% a = find (t==round(data17(1,i)*100)/100 )  ;
% Q(18,a) =1  ;
% 
% end
% 
% for i=1:length(data18)
% a = find (t==round(data18(1,i)*100)/100 )  ;
% Q(19,a) =1  ;
% 
% end
% 
% for i=1:length(data19)
% a = find (t==round(data19(1,i)*100)/100 )  ;
% Q(20,a) =1  ;
% 
% end

% for i=1:length(data20)
% a = find (t==round(data20(1,i)*100)/100 )  ;
% Q(21,a) =1  ;
% 
% end
% 
% for i=1:length(data21)
% a = find (t==round(data21(1,i)*100)/100 )  ;
% Q(22,a) =1  ;
% 
% end
% 
% for i=1:length(data22)
% a = find (t==round(data22(1,i)*100)/100 )  ;
% Q(23,a) =1  ;
% 
% end
% 
% 
% for i=1:length(data23)
% a = find (t==round(data23(1,i)*100)/100 )  ;
% Q(24,a) =1  ;
% 
% end
% 
% for i=1:length(data24)
% a = find (t==round(data24(1,i)*100)/100 )  ;
% Q(25,a) =1  ;
% 
% end
% 
% for i=1:length(data25)
% a = find (t==round(data25(1,i)*100)/100 )  ;
% Q(26,a) =1  ;
% 
% end
% 
% for i=1:length(data26)
% a = find (t==round(data26(1,i)*100)/100 )  ;
% Q(27,a) =1  ;
% 
% end
% 
% for i=1:length(data27)
% a = find (t==round(data27(1,i)*100)/100 )  ;
% Q(28,a) =1  ;
% 
% end
% 
% for i=1:length(data28)
% a = find (t==round(data28(1,i)*100)/100 )  ;
% Q(29,a) =1  ;
% 
% end
% 
% for i=1:length(data29)
% a = find (t==round(data29(1,i)*100)/100 )  ;
% Q(30,a) =1  ;
% 
% end
% 
% for i=1:length(data30)
% a = find (t==round(data30(1,i)*100)/100 )  ;
% Q(31,a) =1  ;
% 
% end
% 
% 
% for i=1:length(data31)
% a = find (t==round(data31(1,i)*100)/100 )  ;
% Q(32,a) =1  ;
% 
% end
% 
% for i=1:length(data32)
% a = find (t==round(data32(1,i)*100)/100 )  ;
% Q(33,a) =1  ;
% 
% end
% 
% for i=1:length(data33)
% a = find (t==round(data33(1,i)*100)/100 )  ;
% Q(34,a) =1  ;
% 
% end
% 
% for i=1:length(data34)
% a = find (t==round(data34(1,i)*100)/100 )  ;
% Q(35,a) =1  ;
% 
% end
% 
% for i=1:length(data35)
% a = find (t==round(data35(1,i)*100)/100 )  ;
% Q(36,a) =1  ;
% 
% end
% 
% for i=1:length(data36)
% a = find (t==round(data36(1,i)*100)/100 )  ;
% Q(37,a) =1  ;
% 
% end
% 
% for i=1:length(data37)
% a = find (t==round(data37(1,i)*100)/100 )  ;
% Q(38,a) =1  ;
% 
% end
% 
% for i=1:length(data38)
% a = find (t==round(data38(1,i)*100)/100 )  ;
% Q(39,a) =1  ;
% 
% end
% 
% for i=1:length(data39)
% a = find (t==round(data39(1,i)*100)/100 )  ;
% Q(40,a) =1  ;
% 
% end
% 
% for i=1:length(data40)
% a = find (t==round(data40(1,i)*100)/100 )  ;
% Q(41,a) =1  ;
% 
% end
% 
% for i=1:length(data41)
% a = find (t==round(data41(1,i)*100)/100 )  ;
% Q(42,a) =1  ;
% 
% end
% 
% for i=1:length(data42)
% a = find (t==round(data42(1,i)*100)/100 )  ;
% Q(43,a) =1  ;
% 
% end
% 
% for i=1:length(data43)
% a = find (t==round(data43(1,i)*100)/100 )  ;
% Q(44,a) =1  ;
% 
% end
% 
% for i=1:length(data44)
% a = find (t==round(data44(1,i)*100)/100 )  ;
% Q(45,a) =1  ;
% 
% end
% 
% for i=1:length(data45)
% a = find (t==round(data45(1,i)*100)/100 )  ;
% Q(46,a) =1  ;
% 
% end
% 
% for i=1:length(data46)
% a = find (t==round(data46(1,i)*100)/100 )  ;
% Q(47,a) =1  ;
% 
% end
% 
% for i=1:length(data47)
% a = find (t==round(data47(1,i)*100)/100 )  ;
% Q(48,a) =1  ;
% 
% end
% 
% for i=1:length(data48)
% a = find (t==round(data48(1,i)*100)/100 )  ;
% Q(49,a) =1  ;
% 
% end
% 
% for i=1:length(data49)
% a = find (t==round(data49(1,i)*100)/100 )  ;
% Q(50,a) =1  ;
% 
% end

%
% figure
% plot(t , Q(1,:))


%%

QQ=Q(:,200001:1200001) ;


for u=1:NN
    
    AVE(u,1) = sum(QQ(u,:)) ;
    AVE(u,1) = 1000*AVE(u,1)/10000  ;
    
end

 AVERAGE = mean(AVE) ;




%%
figure
plot(t(200001:1200001) , QQ(1,:))

%%



tVec=2000/1000:0.01/1000:12000/1000 ;

%figure1=figure('Position', [100, 10, 2000, 800]);
subplot(2,1,1);

hold all;
for trialCount = 1:NN
    clear KKK
    clear spikepos
    clear W
    j=1 ; 
    
    W = QQ(trialCount,:)  ;
    
    
for i=1:length(W)
if W(1,i) > 0
    KKK(1,j) = tVec(1,i)  ;
    j=j+1 ;

end
end


if j>1
    
    spikePos = KKK ;
    
    for spikeCount = 1:length(spikePos)
        plot([spikePos(spikeCount) spikePos(spikeCount)], ...
            [trialCount-0.4 trialCount+0.4], 'k' , 'LineWidth'  , 1.5);
    end
    
    
end   
    
end

ylim([0 NN+1]);
xlim([2 12]);

xlabel('Time (s)')
ylabel('Neuron#')



%%

FFF = (10*1000) - 2.5   ;

MMM = find (t==FFF )  ;

NNNN = (MMM - 1) / 250  ;

UU=zeros(1,NNNN+2)  ;

jj=1 ;


for pp=0:1:NNNN

    P=250*pp+1  ;
    
    UU(1,jj) = 0 ;

for m=1:NN

for n=P:1:(P+250)
    
if QQ(m,n)==1
    
    UU(1,jj) = UU(1,jj)+1  ;
    
end

end

end



jj=jj+1 ; 


end

subplot(2,1,2);

LL = 2000/1000:2.5/1000:12000/1000 ;
LL=LL+(1.25/1000)  ;

bar(LL,UU ,'BarWidth', 1 , 'EdgeColor',[0 0 0])
ylabel('Spikes per bin')
% xlabel('Time (ms)')
xlim([2 12]);
ylim([0 10]);
xlabel('Time (s)')





%%

FFF = (10*1000) - 1   ;

MMM = find (t==FFF )  ;

NNNN = (MMM - 1) / 100  ;


U=zeros(1,NNNN+2)  ;

jj=1 ;


for pp=0:1:NNNN

    P=100*pp+1  ;
    
    U(1,jj) = 0 ;

for m=1:NN

for n=P:1:(P+100)
    
if QQ(m,n)==1
    
    U(1,jj) = U(1,jj)+1  ;
    
end

end

end



jj=jj+1 ; 


end




%%


x= U  ;

% figure
% plot(x)
%
X=fft(x)  ;



%%

Y=X  ;
L=10000 ;
Fs=1000 ;

P2 = abs(Y)/L;
P1 = P2(1:L/2+1);
P1 = 2*P1;

figure2=figure('Position', [100, 10, 500, 400]);
subplot(2,1,1)
f = Fs*(0:(L/2))/L;
plot(f,P1) 
xlabel('Frequency (Hz)')
ylabel('Magnitude')        % Normalized Amplitude


ylim([0 0.4]);



%%
% 
SNR = snr(U,1000)

figure
snr(U,1000);
% 


