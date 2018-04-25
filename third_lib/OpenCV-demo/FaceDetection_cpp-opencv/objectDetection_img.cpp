/**
* @file objectDetection_img.cpp
* @author:wepon 
* @blog: http://2hwp.com
* ���demoʹ��opencvʵ��ͼƬ��������⡢�Լ��滭�����������ȡ�����ȹ��ܡ�
* ÿ������д��һ��������������ֲʹ�á�
* �ο���opencv�����滭��������ģ���ĵ���
*/

#include "opencv2\core\core.hpp"
#include "opencv2\imgproc\imgproc.hpp"
#include"opencv2\highgui\highgui.hpp"
#include "opencv2\objdetect\objdetect.hpp"

#include<sstream>
#include<string>

using namespace cv;
using namespace std;

/*---- detectFaces���� -------
���Ҷ�ͼƬ�е�����������������������(x,y,width,height)
��Ϊ���ܼ���������������Է�������Ϊvetor<Rect>
------------------------------------------------------*/
vector<Rect> detectFaces(Mat img_gray){
	CascadeClassifier faces_cascade;
	faces_cascade.load("haarcascade_frontalface_alt.xml");
	vector<Rect> faces;
	faces_cascade.detectMultiScale(img_gray,faces,1.1, 2, 0|CV_HAAR_SCALE_IMAGE, Size(30, 30) );
	return faces;
}


/*----  drawFaces���� -------
��ԭʼͼƬ������Բ��Ȧ������
------------------------------------------------------*/
void drawFaces(Mat img,vector<Rect> faces){
	namedWindow("draw faces");
	for(size_t i=0;i<faces.size();i++){
		//��ȷ������������������,�ٸ��ݸ����껭��Բ
		Point center(faces[i].x + faces[i].width/2,faces[i].y + faces[i].height/2);
		ellipse(img,center,Size(faces[i].width/2,faces[i].height/1.5),0,0,360,Scalar(0,255,0),2,8,0);
	}
	imshow("draw faces",img);
}


/*----  saveFaces���� -------
��detectFaces����������������Ȼ�󱣴���Щ������
����·���Լ������ļ�������ΪsaveName�����������������
����D�̵�faces�ļ����£�faces�ļ��������ȴ�������
------------------------------------------------------*/
void saveFaces(Mat img,Mat img_gray){
	vector<Rect> faces = detectFaces(img_gray);
	for(size_t i=0; i<faces.size();i++){
		stringstream buffer;
		buffer<<i;
		string saveName = "D:/faces/"+ buffer.str() + ".jpg";
		Rect roi = faces[i];
		imwrite(saveName,img(roi));
	}
}


/*----  detectDrawEyes���� -------
��Ⲣ��Բ�λ����۾�����
����detectFaces����������������Ȼ��������Щ�����������۾���
�������ȿ������Ӿ�ȷ���ֿ��Խ�ʡ��������
------------------------------------------------------*/
void detectDrawEyes(Mat img,Mat img_gray){
	vector<Rect> faces = detectFaces(img_gray);
	for(size_t i=0; i<faces.size();i++){
		Mat faceROI = img_gray(faces[i]);
		CascadeClassifier eyes_cascade;
		eyes_cascade.load("haarcascade_eye.xml");
		vector<Rect> eyes;
		eyes_cascade.detectMultiScale( faceROI, eyes, 1.1, 2, 0 |CV_HAAR_SCALE_IMAGE, Size(30, 30) );
		//��Բ�ο���۾�����
		for(size_t j=0;j<eyes.size();j++){
			Point eyes_center(faces[i].x+eyes[j].x+eyes[j].width/2,faces[i].y+eyes[j].y+eyes[j].height/2);
			int r = cvRound((eyes[j].width + eyes[j].height)*0.25);
			circle(img,eyes_center,r,Scalar(255,0,0),1,8,0);
		}
	}
	namedWindow("detect and draw eyes");
	imshow("detect and draw eyes",img);
}



int main(){
	//��ȡͼ��ת��Ϊ�Ҷ�ͼ���ٽ���ֱ��ͼ���⻯
	Mat img = imread("obama.jpg");
	Mat img_gray;
	cvtColor(img,img_gray,COLOR_BGR2GRAY );
	equalizeHist(img_gray,img_gray);
	//�����������������,��������,�����۾�
	vector<Rect> faces = detectFaces(img_gray);
	saveFaces(img,img_gray);
	drawFaces(img,faces);
	detectDrawEyes(img,img_gray);
	waitKey(0);
	return 0;
}







