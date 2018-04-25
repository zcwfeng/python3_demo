/**
 * @file objectDetection.cpp
 * @author A. Huaman ( based in the classic facedetect.cpp in samples/c )
 * @brief A simplified version of facedetect.cpp, show how to load a cascade classifier and how to find objects (Face + eyes) in a video stream
 */
#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

#include <iostream>
#include <stdio.h>

using namespace std;
using namespace cv;

/** Function Headers */
void detectAndDisplay( Mat frame );

/** Global variables */
//-- Note, either copy these two files from opencv/data/haarscascades to your current folder, or change these locations
String face_cascade_name = "haarcascade_frontalface_alt.xml";
String eyes_cascade_name = "haarcascade_eye_tree_eyeglasses.xml";  //xml�ļ�����ѵ���õ�haar����  
CascadeClassifier face_cascade;
CascadeClassifier eyes_cascade;   //���������������������ֱ����ڼ��faces��eyes
string window_name = "Capture - Face detection";
RNG rng(12345);


/**
 * @function main
 */
int main( void )
{
  VideoCapture capture;    //����ͷ
  Mat frame;               //frame���ڱ�������ͷ��ȡ��ÿ֡����

  //-- 1. ��xml�ļ���ʼ������������
  if( !face_cascade.load( face_cascade_name ) ){ printf("--(!)Error loading\n"); return -1; };
  if( !eyes_cascade.load( eyes_cascade_name ) ){ printf("--(!)Error loading\n"); return -1; };

  //-- 2. ������ͷ
  capture.open( -1 );
  if( capture.isOpened() )
  {
    for(;;)   //ÿ��10ms���һ֡���棬�����û����¼�"C"
    {
      capture >> frame;   //capture >> frame��֡���渳��frame

      //-- 3. �Ը�֡�������faces��eyes���
      if( !frame.empty() )
       { detectAndDisplay( frame ); }
      else
       { printf(" --(!) No captured frame -- Break!"); break; }

      int c = waitKey(20);
      if( (char)c == 'c' ) { break; }

    }
  }
  return 0;
}

/**
 * @function detectAndDisplay
 */
void detectAndDisplay( Mat frame )
{
   std::vector<Rect> faces;     //����faces����������Ϊ����Rect���������϶���(x,y)�����width���߶�heigth��
   Mat frame_gray;

   cvtColor( frame, frame_gray, COLOR_BGR2GRAY );    //cvtColor��������frameת��Ϊ�Ҷ�ͼ��������frame_gray
   equalizeHist( frame_gray, frame_gray );           //equalizeHist������ֱ��ͼ���⻯����ǿ�Աȶ�
   //-- �÷�����face_cascade�������࣬��������faces�detectMultiScale��ߴ��⡣
   face_cascade.detectMultiScale( frame_gray, faces, 1.1, 2, 0|CV_HAAR_SCALE_IMAGE, Size(30, 30) );

   for( size_t i = 0; i < faces.size(); i++ )
    {
      Point center( faces[i].x + faces[i].width/2, faces[i].y + faces[i].height/2 );          //�������ε���������
      ellipse( frame, center, Size( faces[i].width/2, faces[i].height/2), 0, 0, 360, Scalar( 255, 0, 255 ), 2, 8, 0 );   //��frame�ϻ���Բ�������������

      Mat faceROI = frame_gray( faces[i] );     //faceROI�洢�����������֣�ֱ����faceROI�ϼ��eyes������������ͼƬ�ϼ��eyes�����׼�ͽ�ʡ������
      std::vector<Rect> eyes;

      //-- In each face, detect eyes
      eyes_cascade.detectMultiScale( faceROI, eyes, 1.1, 2, 0 |CV_HAAR_SCALE_IMAGE, Size(30, 30) );

      for( size_t j = 0; j < eyes.size(); j++ )
       {
         Point eye_center( faces[i].x + eyes[j].x + eyes[j].width/2, faces[i].y + eyes[j].y + eyes[j].height/2 );
         int radius = cvRound( (eyes[j].width + eyes[j].height)*0.25 );
         circle( frame, eye_center, radius, Scalar( 255, 0, 0 ), 3, 8, 0 );    //��frame�ϻ�Բ�Σ�����۾���
       }
    }
   //-- Show what you got
   imshow( window_name, frame );
}
