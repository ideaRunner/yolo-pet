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
Sphynx
american
Maine
Bombay
Persian
beagle
miniature
pomeranian
Russian
wheaten
yorkshire
english
japanese
Birman
leonberger
pug
Egyptian
chihuahua
shiba
newfoundland
great
saint
german
basset
keeshond
boxer
Ragdoll
Abyssinian
scottish
samoyed
Bengal
havanese
Siamese
staffordshire
British
```
