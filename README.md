# YOLOv8 Implementation From Scratch

A custom implementation of YOLOv8 (You Only Look Once) object detection model built entirely from scratch for deep learning research and educational purposes.

## Project Overview

This project implements the YOLOv8 architecture from the ground up, focusing on understanding the core concepts and mechanics behind modern object detection algorithms. While our model didn't achieve state-of-the-art accuracy due to limited computational resources and dataset size, the journey of building YOLO from scratch provided invaluable insights into:

- Object detection fundamentals
- Anchor-free detection mechanisms  
- Feature pyramid networks
- Loss function design for object detection
- Non-Maximum Suppression (NMS) algorithms

## Features

- **Complete YOLOv8 Architecture**: Built from scratch using PyTorch
- **Anchor-Free Detection**: Modern approach eliminating the need for predefined anchors
- **Loss Functions**: Implementation of classification, regression, and objectness losses
- **Data Pipeline**: Custom data loaders supporting COCO format annotations
- **Training Loop**: Complete training pipeline

## 📊 Dataset Structure

```
Data/
├── Train/
│   ├── images/
│   └── labels/
│       ├── *.txt files
│       ├── annotations.csv
│       └── annotations.coco.json
├── Valid/
│   ├── images/
│   └── labels/
│       ├── *.txt files
│       ├── annotations.csv
│       └── annotations.coco.json
└── data.yaml
```

## 🛠Installation

Clone the repository:
```bash
git clone https://github.com/your-username/yolov8-from-scratch.git
cd yolov8-from-scratch
```

Install required dependencies:
```bash
pip install torch torchvision
pip install opencv-python
pip install matplotlib
pip install pandas
pip install pyyaml
pip install tqdm
```

## Architecture Details

Our YOLOv8 implementation includes:

- **Backbone**: CSPDarknet with Cross Stage Partial connections
- **Neck**: Feature Pyramid Network (FPN) + Path Aggregation Network (PAN)
- **Head**: Anchor-free detection head with decoupled classification and regression branches
- **Activation**: SiLU (Sigmoid Linear Unit) activation function throughout the network
- **Normalization**: Batch normalization for stable training

## Model Performance

**Note**: Due to limited computational resources and dataset size, our model's accuracy is below commercial implementations. However, the focus was on learning and understanding the underlying mechanisms rather than achieving optimal performance.

- **Training Loss**: 0.647 (Converged after ~80 epochs)
- **Validation mAP**: 0.692 (Limited by dataset size)

## Learning Outcomes

Building YOLOv8 from scratch helped us understand:

1. **Object Detection Pipeline**: End-to-end understanding of detection workflow
2. **Anchor-Free Methods**: Modern approaches that eliminate anchor box dependencies
3. **Feature Pyramid Networks**: Multi-scale feature extraction and fusion
4. **Training Strategies**: Data augmentation, learning rate scheduling, and optimization techniques

## 🤝 Contributors

This project was developed by students from **Delhi Technological University**:

- **Pranay** - Architecture design and implementation
- **Aarushi** - Data preprocessing and training pipeline  
- **Divansu** - Loss functions and evaluation metrics

## Key Learnings

The most valuable aspect of this project wasn't achieving high accuracy, but rather the deep understanding gained by implementing every component from scratch. This approach allowed us to:

- Debug and understand each component's role
- Experiment with different architectural choices
- Appreciate the complexity behind "simple" object detection

##  Future Improvements

- Implement data augmentation strategies (Mosaic, MixUp)
- Add support for larger datasets
- Optimize training with mixed precision
- Implement model quantization for deployment
- Add support for custom dataset formats

## 📚 References

- [YOLOv8 Official Paper](https://arxiv.org/abs/2408.15857)
- [PyTorch Official Documentation](https://docs.pytorch.org/docs/stable/index.html)

---

*Built with ❤️ by DTU students for learning and research purposes*
