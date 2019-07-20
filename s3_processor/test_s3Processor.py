from unittest import TestCase
from s3_processor import S3Processor

class TestS3Processor(TestCase):
    pass


class TestS3Processor(TestCase):
    def test_createPartition(self):
        pass
        #self.fail()

    def test_writeObject(self):
        pass
        #self.fail()

    def test_createS3Key(self):
        my_dict = dict()
        my_dict['col_name1'] = 'col_value1'
        my_dict['col_name2'] = 'col_value2'
        createdKey = S3Processor.S3Processor('test_bucket').createS3Key(my_dict)
        print('createdKey' + createdKey)
        TestCase.assertEquals(self, createdKey, 'col_name1=col_value1/col_name2=col_value2')
