# Image Forgery Detection Using Machine Learning - The AI Hackathon
## Description:

In this project, we present a cutting-edge method for **Image Forgery Detection** using a novel combination of Error Level Analysis (ELA) and **Convolutional Neural Networks (CNNs)**. Our approach stands out for its robustness and high accuracy.

![image](https://github.com/user-attachments/assets/6d67f060-4be3-4a25-8238-58b58613529e)

### Key Highlights:

- **Novel Approach:** Learn how we combine ELA with CNNs, where the output of ELA is used as input for the CNN, enhancing the detection of image forgeries.
  
- **Innovation and Results:** Discover the innovative aspects of our method and see how it achieved an impressive accuracy of **90.3%** in detecting various types of image forgeries. This accuracy can be fine-tuned to produce even better results.
  
## **Dataset Used:**
We used the **CASIA 2.0** dataset available on Kaggle because of its reliability, robustness, and versatility in terms of the types of image forgeries present. This is a well-balanced dataset containing over **12,000+** images.
- https://www.kaggle.com/datasets/divg07/casia-20-image-tampering-detection-dataset

### Algorithms Implemented:

1. **Error Level Analysis (ELA)**:
   - ELA reveals differences in compression levels within an image, which can detect edited or manipulated regions.
   - **Benefit**: Helps detect subtle differences in tampered images that might not be visible to the naked eye.

2. **Convolutional Neural Networks (CNNs)**:
   - CNNs automatically learn visual patterns like textures and discrepancies that might indicate image forgeries.
   - **Benefit**: Excels at image classification tasks by learning complex features from the input data.

### High-level Solution Architecture:

![image](https://github.com/user-attachments/assets/603f182e-cb88-44ed-8c78-865f4d5a6f74)

1. **Input Image**: The input image is processed using **Error Level Analysis (ELA)** to highlight compression inconsistencies. This gives the CNN model a better idea of which parts of the image are prone to be forged.
2. **Convolutional Neural Network (CNN)**: The ELA output is fed into the CNN, where multiple convolutional layers extract features, and pooling layers reduce dimensions. Dropout is applied to avoid overfitting.
3. **Fully Connected Layer**: The features from the CNN are passed through dense layers to interpret the image’s forged or authentic characteristics.
4. **Output**: The system classifies the image as either **forged or authentic** based on the processed features.

**Link to video**: https://youtu.be/0iSTFComJ5I

> **Note:** Please be aware that due to some last-minute technical issues, a part of the video has inaudible audio. We apologize for any inconvenience this may cause and appreciate your understanding.

### Next Steps for Image Forgery Detection:

1. **Real-Time Forgery Detection**:  
   - Optimize the system for real-time detection on platforms like social media using faster inference and scalable deployment.

2. **Improving Accuracy**:  
   - Use advanced models like ResNet or Transformers and apply transfer learning to improve detection accuracy.

3. **Enhanced Forgery Detection**:  
   - Integrate techniques for detecting sophisticated forgeries like DeepFakes to increase model robustness.
