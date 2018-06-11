import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import shutil
import random
classes = ['Abyssinian', 'Bengal', 'Birman', 'Bombay', 'British', 'Egyptian', 'Maine', 'Persian', 'Ragdoll', 'Russian', 'Siamese', 'Sphynx', 'american', 'basset', 'beagle', 'boxer', 'chihuahua', 'english', 'german', 'great', 'havanese', 'japanese', 'keeshond', 'leonberger', 'miniature', 'newfoundland', 'pomeranian', 'pug', 'saint', 'samoyed', 'scottish', 'shiba', 'staffordshire', 'wheaten', 'yorkshire']

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_annotation(image_id):
    try:
        in_file = open('annotations/xmls/%s.xml' % image_id)
        out_file = open('labels/%s.txt' % image_id, 'w')
        tree=ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)
        breeds = root.find('filename').text
        cls = breeds[:breeds.find('_')]

        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            # breeds = string.capwords(obj.find('name').text)+'_'+cls
            if cls not in classes or int(difficult) == 1:
                continue
            # if int(difficult) == 1:
            #     continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
            return True
    except:
        return False


def generate():
    wd = getcwd()
    if not os.path.exists('labels'):
        os.makedirs('labels')

    train_image_ids = []
    with open('annotations/trainval.txt') as f:
        lines = f.readlines()
        for x in lines:
            train_image_ids.append(x.split(' ')[0])

    test_image_ids = []
    with open('annotations/test.txt') as f:
        lines = f.readlines()
        for x in lines:
            test_image_ids.append(x.split(' ')[0])

    train_list_file = open('Train_List.txt', 'w')
    val_list_file = open('Val_List.txt', 'w')
    num_train =0
    num_val =0
    for image_id in train_image_ids:
        if convert_annotation(image_id):
            if random.random() > 0.1:
                train_list_file.write('%s/JPEGImages/%s.jpg\n' % (wd, image_id))
                num_train = num_train + 1
            else:
                val_list_file.write('%s/JPEGImages/%s.jpg\n' % (wd, image_id))
                num_val = num_val + 1
    print("Train files: {0}, Val files: {1}.".format(num_train, num_val))
    train_list_file.close()
    val_list_file.close()


def clean():
    wd = getcwd()
    os.remove(wd+'/Train_List.txt')
    os.remove(wd+'/Val_List.txt')
    shutil.rmtree('labels')
    print("Clean Finished.")


if __name__ == '__main__':
    import argparse
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="'generate' labels or 'clean' on PetSet")
    parser.add_argument("command",
                        metavar="<command>",
                        help="'generate' labels or 'clean' on PetSet")

    args = parser.parse_args()
    print("Command: ", args.command)
    if args.command == "generate":
        generate()
    # elif args.command == "back":
    #     val_back_train()
    elif args.command == "clean":
        clean()
    # elif args.command == "avg":
    #     average_dataset()
    else:
        print("Command error, 'generate' or 'back'")




# cannot find some xml files