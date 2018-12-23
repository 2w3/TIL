



1.시장이 원하는 사람 멀티플레이어(DEVOPS)

https://brunch.co.kr/@topasvga/75

- DEVOPS

  1. 멀티 플레이어를 원한다.

     DEVOPS 시대

     DEV + OPS (개발자 + 운영담당자)

  2. 자동화를 잘하는 인력은 필수다.

     자동화툴 Ansible은 필수

  3. 개발자도 인프라를 알아야 한다.

  4. 클라우드 시대로 간다. 인프라 담당자의 위기와 기회가 된다.

     개발에 집중해야 서비스가 더 개선되고 안정화 된다.



2.AWS 용어 알아보기

https://brunch.co.kr/@topasvga/76

+ 기존 인프라 AWS 용어

1. 네트워크

   VPC(Virtual Private Cloud, 가상 개인 네트워크)

   외부와 연동이 되는 Public과 외부에서 접속하지 못하는 DB서버 네트워크인 Private를 구축하게 해준다.

   VPC에서 Subnet을 나누어 정책을 적용한다.

   네트워크 할당할때 사용

2. 보안장비/방화벽 Firewall == Security Group 

   Security Group

   인터넷에서 네트워크를 차단, 허용

3. L4

   ELB(Elastic Load Balancer) 
   서버 이중화 장비

   서버 이중화를 위해 부하 분산시 사용

4. Server

   EC2(Elastic Compute Cloud)

5. DNS

   ROUTE53

   도메인을 관리하고 글로벌 이중화 서비스가 되도록 

   GSLB기능도 제공

6. DB

   RDS(Relational Database Service)와 NoSQL

7. Storage

   NAS = S3(Simple Storage Service) = Object Storage

8. CDN(Content Delivery Network)

   CLOUD FRONT

   대규모 파일

   이미지 서비스

9. EBS(Elastic Block Store)

   Block Storage

   Hard Disk

   보통 OS나 DB영역에 사용한다

10. AMI(Amazon Machine Image)

    Linux와 Windows OS Server Image

11. Public IP

    변경되는 공인 IP

    외부에서 접속가능하나 AWS Instance 시작할때 임의 IP로 할당된다.

    변경이 되는 IP

    인터넷 서비스 목적이라면, 변경이 되지 않는 EIP를 할당받아 사용하도록 한다.

12. EIP(Elastic IP)

    Public IP이나 한번 할당되면 변하지 않는 공인 IP

    고정 공인 IP

    인터넷 서비스할때 EIP를 사용한다

    DNS에 매칭한다

13. IGW(Internet GateWay)

    인터넷으로 나가기 위한 통로

    VPC는 폐쇄된 네트워크인테 외부와 통신하기 위해서

    IGW를 통해 통신한다

14. Routes

    VPC는 여러개의 Subnet으로 나눌수 있고,

    Subnet(Zone)간 통신 경로를 잡아주는 것이다.


3.AWS가입과 무료서버 1대 받기

https://brunch.co.kr/@topasvga/77

1. 가입하기
2. 네크워크 만들기
3. 무료 EC2서버 1대 만들기
4. 서버에 접속하기



4.AWS 요금 알아보기

https://brunch.co.kr/@topasvga/78

1. AWS Console 오른쪽 위 메뉴에서 금액 확인할 수 있다
2. Route53 요금
3. Elastic IP(고정 공인 IP)
4. VPC(네트워크)
5. 빌링관리 팁





5.[AWS] 게임웹 구축, VPC, ELB, Route53

https://brunch.co.kr/@topasvga/79

Network, Security(Firewall), L4, Server, DNS Configuration

1. 네트워크 VPC 설정
2. 이중화를 위해 C-Class단위 2개로 Subnet을 나눈다.
3. Subnet 하나를 더 만든다.
4. Gateway를 생성하고 Network에 연결한다.
5. 모든 Packet을(0.0.0.0/0) 게이트웨이(game-web-igw1)로 가도록 설정한다.
6. 이제 만들어진 Subnet에 각각 Server 1대를 생성해보자.
7. Next: Configure Instance Details 클릭
8. 10.0.10.0/24에 서버 1대 생성
9. 서버이름을 지정한다.
10. 보안그룹 설정
11. 이제 2개의 서버가 만들어졌다.
12. 임시로 Elastic IPs를 받아 서버와 매칭한다.
13. 보안 그룹 설정한다.
14. 리눅스 서버에서 ssh로 서버 접속해 ftp와 apache를 설치해보자.
15. ELB 설정한다.
16. 80에 대해 Load Balancer 설정한다.
17. ELB가 설정되었다.
18. Monitoring 부분에 Health Hosts가 2개 ON되어 있는것 확인이 가능하다.
19. 브라우저로 각 서버 공인 IP(Elastic IPs)로도 접속해 사이트가 뜨는것을 확인한다.
20. route53에서 cname으로 DNS name을 설정한다.
21. 서버 1대의 apache를 다운시켜 본다.
22. 이제 정상동작하는게 확인되었다.



6.AWS Service, 서비스들 알아보자

https://brunch.co.kr/@topasvga/80

AWS 구성

1. 사용자
2. 관리자 페이지
3. 클라우드 인프라



AWS Words

AWS는 Security Group, VPC, EC2, S3, RDS로 구성되어 있다.

기존 인프라의 보안, 네트워크, 서버, 스토리지, 데이터베이스와 같다.



<1> 용어 요약

1. 서버 == EC2
2. 사용자계정 및 그룹관리 == IAM
3. 데이터베이스 == RDS == DB
4. 네트워킹 == VPC
5. L4 == ELB
6. Storage == S3 == NAS
7. Firewall == Security Group
8. Network ACL == NACL



<2> 서비스 2가지

AWS 기초서비스

1. 컴퓨팅 서비스 

   EC2 Container Service

   서버와 서버 이중화

   ELB(Elastic Load Balancing) == L4

   Lamda(이벤트응답으로 코드실행)

   Auto Scaling(서버 자동증설)

2. 네트워킹

   네트워크 구성, VPC

   DNS, Route53

   Direct Connect(데이터 전용선)

   DNS

   Cloud Front, CDN

3. 스토리지

   데이터 저장공간

   S3, 일반 스토리지

   Glacier, 저렴한 스토리지

   EBS, 빠른 블록 스토어

4. 관리 및 보안

   계정관리와 모니터링 시스템

   IAM, 사용자계정 및 그룹관리

   Cloud Watch, 모니터링 시스템

   Cloud Trail, 계정에 대한 API호출기록

5. 어플리케이션

   Work Spaces, 클라우드기간 데스크톱을 간편하게 프로비저닝

   Work Docs, 스토리지 및 공유 서비스





AWS 플랫폼 서비스

1. Database Service

   RDS, Relational DB/Mysql, Oracle etc.

   NoSQL, DynamoDB

   DW Configuration, 페타규모, Redishift

   Cache Cluster, ElasticCache

2. Analyze

   Data Collect, Kinesis

   Data Processing, EMR

   Data Access, 변환처리, Data Pipeline

3. Web Service

   Search, Cloud Search

   Transaction Email, SES

   Status Tracking, 작업조정, SWF

4. Deployment and Management

   Ops Works

   Resource Template Creation, CloudFormation

   Automatic Deployment, Elastic Beanstalk

   CodeDeploy

5. Mobile Service

   SNS, Puth Notification to Mobile

   Cognito, 사용자 데이터 동기화 및 자격증명

   Mobile Analytics, 모바일 분석, 보고서

   Elastic Cache, 캐시 클러스터

   참고: 스택이란 함께 관리하고자 하는 컴퓨터 인프라와 애플리케이션을 나타냅니다.



서버 제공 서비스 EC2(Elastic Compute Cloud)

크기 조정 가능한 서버

1시간 단위 과금

1년 예약하면 비용 절감



EC2 사용하는 순서

1. Region을 정함(생성 지역 설정)
2. Amazon Machine Image(AMI)에서 EC2 Instance를 시작
3. CPU, Memory, Storage, Network 요구사항에 따라 Instance유형을 선택
4. Network IP, Security Group, Storage Volume, Tag, Key Pair를 구성함



Intel EC2 Instance

1. Computing Optimization C4
2. Memory Optimization R3
3. I/O Optimization I2
4. Balance 조정 M3
5. 범용 및 순간확장 T2
6. Storage Optimization HS1



EC2 Container Service == Docker Conatiner Resource



Lamda == Event Response Code Run

Computing Resource Automatic Management



Auto Scaling

EC2 용량을 자동으로 조정하는 것



Auto Scaling 동작, 3가지 서비스의 조화

1) Auto Scaling

기 정의된 필요한 서버 생성

2) ELB(Elastic Load Balancing)

L4로 서버를 서비스에 추가

3) Cloud Watch

크기 조정 정책

모니터링

5분동안 CPU사용률이 xx%이상이면 적용



AWS 네트워킹 제품

1. Virtual Private Cloud(VPC), 가상 네트워크

   예전의 데이터센터, 네트워크를 말함

   Private하고 Isolation된 공간

   Private IP 범위지정

   VPN 연결

   Subnet 분할

   Access Control List

   IP를 사용할때 돈을 받지 않음

   사용하지 않을때 돈을 받음(반납을 위해)

2. Direct Connect(데이터 전용선 서비스), 고객과 AWS IDC간 직접 데이터 전용선을 연결하는 서비스

3. Route 53(DNS), DNS Service

   도메인 이름 등록 제공

   TTL은 1분

   도메인 구매도 가능

4. Elastic Load Balancing, ELB, L4, 서버 부하 분산



+ AWS 스토리지 제품 및 서비스

  1. S3(Simple Storage Service), NAS같은 Storage

     기본적으로 온라인, HTTP 액세스 제공

     버킷내에 객체로 저장함

     계정당 100개 버킷 보유가능

     실제 사용한만큼만 지불

     최소 요금 없음

     월별 청구

     S3 사용법

     1. S3에 컨텐츠 올리기
     2. Public으로 권한 허용
     3. Static Web Hosting허용하면 Web에 노출된다
        - 인터넷 액세스 가능

  2. Glacier, 데이터 백업용으로 적합한 Storage

  3. EBS(Elastic Block Store), 서버 저장장치 

  4. Storage Gateway

  5. Import/Export 

  6. Cloud Front, CDN






1. 가상서버는 OS, WEB/WAS, 어플리케이션, DB 설치된 이미지를 준비
2. 네트워크장비 L4를 이용하여 디폴트 이중화
3. L7 Check설정을 통한 WAS, DB장애까지 모니터링
4. 웹 Cache등 기술플랫폼을 적용
5. CDN을 활용
6. MySQL DB 이중화를 MMM을 활용
7. 사용자가 늘어 DB성능이 부족한 경우, Read-Only DB를 사용하여 분산
8. 주간단위로 인프라 모니터링 리뷰하는 시간
9. 회사 핵심 서비스는 데이터센터 이중화
10. IDC 전체 서버 이전작업시 GSLB기능을 이용해 가중치를 두어 영향을 최소화
11. 장애가 길어질경우 공지페이지 서버군을 준비
12. 정기점검시 사용자가 필수 서비스는 받도록 Read-Only DB를 활용
13. 





reference url





