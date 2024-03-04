from PIL import Image
import os

def combine_imgs_pdf(folder_path, pdf_file_path):
    """
    Combine all images in a folder into a PDF, maintaining their original orientation and making their widths consistent.
    Args:
        folder_path (str): Source folder path.
        pdf_file_path (str): Output PDF file path.
    """
    files = os.listdir(folder_path)
    image_files = [f for f in files if f.endswith(('.png', '.jpg'))]
    image_files.sort()

    # Load images
    images = [Image.open(os.path.join(folder_path, f)) for f in image_files]

    # Find the maximum width
    max_width = max(img.size[0] for img in images)

    # Resize images to have the same width while maintaining aspect ratio
    resized_images = []
    for img in images:
        if img.size[0] != max_width:
            aspect_ratio = img.size[1] / img.size[0]
            new_height = int(aspect_ratio * max_width)
            resized_img = img.resize((max_width, new_height))
        else:
            resized_img = img

        resized_images.append(resized_img.convert('RGB') if img.mode != 'RGB' else resized_img)

    # Save as PDF
    resized_images[0].save(pdf_file_path, save_all=True, append_images=resized_images[1:])

if __name__ == "__main__":
    folder = './'
    pdf_file_name = input("输出文件名：")
    pdf_file_path = os.path.join(folder, pdf_file_name + '.pdf')
    combine_imgs_pdf(folder, pdf_file_path)
