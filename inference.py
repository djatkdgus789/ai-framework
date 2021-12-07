import torch
import torchvision
import time


# Instantiate a PyTorch Module and move it to a GPU
batch = 1
i = 1
while i != 9:
    start = time.time()
    model = torchvision.models.vgg16()
    model.eval()
    # Prepare a dummy input
    input_shape = [batch, 3, 224, 224]
    # Execute the object
    rand_input = torch.rand(*input_shape)
    output = model(rand_input)
    print("batch : ", batch)
    print("time : ", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

    batch = batch * 2
    i = i +1
