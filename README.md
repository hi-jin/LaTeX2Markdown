# Polygon2Programmers
![image](https://github.com/sion-k/Polygon2Programmers/assets/44183313/18c64ea6-9290-478e-8316-1259b729035e)

Polygon에서 작업한 결과물을 프로그래머스에 올릴 때 사용하려고 만든 변환기입니다. 그 외에도 기타 필요한 유용한 기능을 포함하고있습니다.

## 기능

### LaTeX을 markdown으로 변환

Polygon으로 문제를 작성하면 문제 지문은 LaTeX으로 작성해야합니다. 하지만 프로그래머스 문제 지문은 markdown만 지원하기 때문에, 이 변환기는 LaTeX을 markdown으로 변환해줍니다.

프로그래머스에서 수식을 입력하기 위해서 LaTeX 수식을 빌드한 후에 SVG로 변환합니다. 그리고 이 SVG를 base64로 인코딩한 이미지 태그로 삽입합니다.

### 테스트 케이스 확장자 변경

Polygon으로 데이터를 작성하면 데이터는 각각 `01`, `01.a`와 같은 형식으로 저장됩니다. 하지만 프로그래머스에서 데이터 파일 이름은 `01.in.txt`, `01.out.txt`와 같이 `in.txt`, `out.txt`로 끝나야 합니다. 이 변환기는 데이터 파일의 확장자를 `in.txt`, `out.txt`로 변경해줍니다.

### LaTeX Editorial 초안 생성

각각의 문제의 Editorial에 반드시 포함되어야 하는 문제 지문, 입출력 조건, 문제 정답 코드, 예제 입출력 등을 포함한 LaTeX 초안을 생성해줍니다.

### TODO: 프로그래머스 문제 업로드, 등록

셀레니움을 이용해 주어진 Polygon package를 프로그래머스에 업로드합니다.
