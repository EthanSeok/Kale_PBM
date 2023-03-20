## 진행 상황

* 엽수 증가 모델 
* 엽면적 지수 (LAI) 모델 

<br>

<br>

## 참고 글

* [모델링 - 파이썬으로 FvCB A-Ci 커브 그려보기](https://ethanseok.github.io/2023-01-26/FvCB-post)
* [모델링 - Michaelis - Menten과 Arrhenius eqn의 관계](https://ethanseok.github.io/2023-02-20/mm-post)
* [모델링 - Newton-Raphson method로 모수 최적화](https://ethanseok.github.io/2023-02-28/newton-post)
* [모델링 - 여러가지 작물생육 모델 돌려보기 -1부](https://ethanseok.github.io/2023-03-01/crop_model1-post)
* [모델링 - 여러가지 작물생육 모델 돌려보기 -2부](https://ethanseok.github.io/2023-03-02/crop_model2-post)
* [모델링 - 케일 엽수 증가 모델 with AIHub](https://ethanseok.github.io/2023-03-08/leaf_number-post)
* [모델링 - 케일 LAI 예측 모델 with AIHub](https://ethanseok.github.io/2023-03-15/lai_kale-post)

<br>

<br>

## Cabbage_PBM으로 부터 수정 사항

### pykale.py
```python
density = 24 # kale
iniLN = 3 # kale
daysRoot = 2 # kale
pLeafForm = 0.8 # kale
```
<br>

### fraction.py
sun incl 수정 및 sunght 고정
```python
def radFraction(self, doy, hour, PPFD, LAI):
  
                     중략 
                     
    incl = np.arcsin(sin_a + cos_b * np.cos(ha))           # sun inclination   rad
    sunhgt = np.arcsin(max(0.05,sin_a + cos_b * np.cos(ha)))                    # solar height   rad
    if sunhgt > 0.051: sunhgt = 1

```

![image](https://user-images.githubusercontent.com/93086581/224602314-55be6012-3421-4cf7-916a-8a9e4b9d1e8e.png)

<br>

### stage.py

Param
```python
Rxleaf  = 0.4 
Toleaf  = 24.1
```

<br>

엽수 증가식
```python
def midRateLN(self, Ta):
    # calculation leaf number
    if (Ta > 0.0) and (Ta < Txleaf): 
        leafRate = Rxleaf * 7.54453390241129 / self.leafNumber* ((Txleaf-Ta)/(Txleaf-Toleaf))*(Ta/Toleaf)**(Toleaf/(Txleaf-Toleaf)) # Kale
        leafRate = leafRate * conv
    else:
        leafRate = 0.0
    # print(leafRate)
    return leafRate
```

<br>

엽장 분포
```python
def eachLenDistribution(self, leafnumber):  ## internal function
    eachLenDist = []
    if leafnumber < 3:                    ## limit of leafnumber 3장 보다 작을 경우 오류 방지
        for i in range(leafnumber):
            eachLenDist.append(1.0)
    else:
        a = 11.258377311819*np.log(leafnumber) - 9.66635313517988 # kale
        b = 0.0929621981017087*(leafnumber) + 1.85657767789082 # kale
        for i in range(1,leafnumber+1):
            eachLen = a * np.exp(-0.5 * ((i - b) / b)**2)
            eachLenDist.append(eachLen)
    # print(eachLenDist)
    return eachLenDist
```

<br>

엽면적 계산
```python
def eachLeafArea(self, eachLenDist):       ## internal function
    eachLeafArea = [0.4179*each**2 + 3.6915*each - 2.128 for each in eachLenDist] # kale
    # print(eachLeafArea)
    return eachLeafArea
```
<br>

케일 엽면적 합산 함수 추가
```python
def kaleLeafArea(self, leafnumber):
    a = self.eachLenDistribution(leafnumber)
    leafArea = self.eachLeafArea(a)
    totalArea = sum(leafArea)
    return totalArea
```

<br>

케일 LAI 계산 수정
```python
def calcBD(self, Ta, dap):
    
            중략       
    
    ###### LAI calculation
    leafNumber = self.leafNumber
    plantDensity = self.plantDensity
    kaleLeafArea = self.kaleLeafArea(int(leafNumber))
    lai  =  kaleLeafArea * plantDensity / 10000
    self.lai = lai
```

<br>

verdvs max를 min으로 수정
```python
def calcVerdvs(self, Ta):
    Ta  = max(Ta, 0.01)
    rate = np.exp(-1*(np.log(Ta/optVer)**4))
    self.sumVer += rate * conv
    self.verdvs = min(1, self.sumVer/satVer)
```

<br>

<br>

## Python 실행 결과
### 20230316
![model_results](https://user-images.githubusercontent.com/93086581/226378358-52d3707d-e496-4381-bd34-40eb8d479ab1.png)
![LAI_compare](https://user-images.githubusercontent.com/93086581/226378439-98320d21-dc7f-494f-b2f8-424b2f82102f.png)
![image](https://user-images.githubusercontent.com/93086581/225551605-c25da5dc-6095-4b45-a28a-38328b2a8abd.png)

