import cv2


class SubwayVision:

    def __init__(self, image_path):
        self.image_path = image_path

    def load_image(self):
        image = cv2.imread(self.image_path)

        if image is None:
            raise FileNotFoundError(
                f"Image not found: {self.image_path}"
            )

        return image

    def detect_lanes(self, image):

        height, width = image.shape[:2]

        # قسمت پایین/میانی بازی
        roi = image[
            int(height * 0.30):
            int(height * 0.90),
            0:width
        ]

        lane_width = width / 3

        lanes = []

        for i in range(3):

            x1 = int(i * lane_width)
            x2 = int((i + 1) * lane_width)

            lane = roi[:, x1:x2]

            lanes.append(lane)

        return lanes

    def analyze(self):

        image = self.load_image()

        lanes = self.detect_lanes(image)

        print("تصویر دریافت شد ✅")
        print("تعداد لاین‌ها:", len(lanes))

        for i, lane in enumerate(lanes):

            h, w = lane.shape[:2]

            print(
                f"لاین {i + 1}: "
                f"{w}x{h}"
            )


if __name__ == "__main__":

    vision = SubwayVision("screen.png")

    vision.analyze()
