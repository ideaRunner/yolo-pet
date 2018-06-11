# YOLO-Pets
Real-time pet detection and recognition

### Prepared

#### Clone this repo
```
git clone https://github.com/ideaRunner/yolo-pet.git
cd yolo-pet
```
#### Download Pet Dataset
The Oxford-IIIT [Pet Dataset](http://www.robots.ox.ac.uk/~vgg/data/pets/)

You can download the images and annotations by

```
wget -c http://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
wget -c http://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz
```
Unzip

```
tar -xvf images.tar.gz
tar -xvf annotations.tar.gz
```
```
mv images JPEGImages
```
#### [YOLO](https://pjreddie.com/darknet/yolo/)
```
git clone https://github.com/pjreddie/darknet
cd darknet
make
```
Download Pretrained Convolutional Weights of YOLO

`wget https://pjreddie.com/media/files/darknet53.conv.74`

### Configuration

- Generate label files

```
cd ..
python pet_label generate
```

Then there will be a `Train_List.txt` file and `Val_List.txt` file in the root directory and labels in `labels` directory


- Edit configure files

```
vim darknet/cfg/pet.data
```
copy, paste and save

```
classes= 35
train  = Your/Own/Path/Train_List.txt
valid  = Your/Own/Path/Val_List.txt
names = data/pet.names
backup = pet_backup
```
Don't forget to change the path as you generate before.

```
vim darknet/data/pet.names
```
copy, paste and save 
 
```
Abyssinian
Bengal
Birman
Bombay
British
Egyptian
Maine
Persian
Ragdoll
Russian
Siamese
Sphynx
american
basset
beagle
boxer
chihuahua
english
german
great
havanese
japanese
keeshond
leonberger
miniature
newfoundland
pomeranian
pug
saint
samoyed
scottish
shiba
staffordshire
wheaten
yorkshire
```
yolov3.cfg

```
mv darknet/cfg/yolov3-voc.cfg darknet/cfg/yolov3-pet.cfg 
vim darknet/cfg/yolov3-pet.cfg 
```
Edit the last serveal lines, change fliters to 120 and classes to 35

```
mkdir darknet/pet_backups
```

- Modify Some Code

(1) In src/yolo.c, change class numbers and class names. (And also the paths to the training data and the annotations, i.e., the list we obtained from step 2. )

If we want to train new classes, in order to display correct png Label files, we also need to moidify and rundata/labels/make_labels

(2) In src/yolo_kernels.cu, change class numbers.

(3) Now we are able to train with new classes, but there is one more thing to deal with. In YOLO, the number of parameters of the second last layer is not arbitrary, instead it is defined by some other parameters including the number of classes, the side(number of splits of the whole image). Please read the paper.

(5 x 2 + number_of_classes) x 7 x 7, as an example, assuming no other parameters are modified.

Therefore, in cfg/yolo.cfg, change the “output” in line 218, and “classes” in line 222.

(4) Now we are good to go. If we need to change the number of layers and experiment with various parameters, just mess with the cfg file. For the original yolo configuration, we have the pre-trained weights to start from. For arbitrary configuration, I’m afraid we have to generate pre-trained model ourselves.
(5)

```

char *pet_names[] = {"Abyssinian", "Bengal", "Birman", "Bombay", "British", "Egyptian", "Maine", "Persian", "Ragdoll", "Russian", "Siamese", "Sphynx", "american", "basset", "beagle", "boxer", "chihuahua", "english", "german", "great", "havanese", "japanese", "keeshond", "leonberger", "miniature", "newfoundland", "pomeranian", "pug", "saint", "samoyed", "scottish", "shiba", "staffordshire", "wheaten", "yorkshire"}



draw_detections(im, dets, l.side*l.side*l.n, thresh, pet_names, alphabet, 35);

```