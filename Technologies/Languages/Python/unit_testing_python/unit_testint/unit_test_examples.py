import unittest
from pyspark.sql import col
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, BooleanType, LongType, NullType

# We create a class from unittest.TestCase and we add some methods
class TestMKSilver(unittest.TestCase):
  
  def test_assert_count(self, df, lenght):
    # checks if a dataframe has a minimnum lenght equal to the input variable lenght
    con = df.count()
    if lenght==1:
      try:
        self.assertGreaterEqual(con, lenght, f'Not greater or equal to {str(lenght)}')
      except AssertionError:
        raise AssertionError('The input df is empty')
    else:
      try:
        self.assertGreaterEqual(con, lenght, f'Not greater or equal to {str(lenght)}')
      except AssertionError:
        raise AssertionError('The input df has not the expected lenght')
  
  def test_assert_schema(self, df, expected_schema):
    # checks if a df has the same schema as the provided variable expected_schema    
    field_list = lambda fields: (fields.name, fields.dataType, fields.nullable)
    df_schema = sorted([*map(field_list, df.schema.fields)])
    expected_df_schema = sorted([*map(field_list, expected_schema.fields)])
    
    try:
      self.assertEqual(df_schema, expected_df_schema)
    except AssertionError:
      raise AssertionError('The input df has not the expected schema')
      
  def test_assert_load(self, df, expected_schema):
    # Checks whether the df is empty and if has a given schema
    self.test_assert_count(df, 1)
    self.test_assert_schema(df, expected_schema)
      
class TestContactsMK(TestMKSilver):
  # son class of TestMKSilver, created to provide a schema to use the method test_assert_load from TestMKSilver
  def test_contacts_mk(self, df):
    expected_schema = StructType([
      StructField('ID',StringType(),True),
      StructField('EMAIL',StringType(),True),
      StructField('ID_VERSION',StringType(),True),
      StructField('COD_PARK',StringType(),True),
      StructField('COD_CEV',StringType(),True),
      StructField('COD_INT_CONTACT',StringType(),True),
      StructField('COD_PARENT_CONTACT',StringType(),True),
      StructField('NAME',StringType(),True),
      StructField('FAMILY_NAME_1',StringType(),True),
      StructField('FAMILY_NAME_2',StringType(),True),
      StructField('COD_GENDER',StringType(),True),
      StructField('BIRTHDATE',TimestampType(),True),
      StructField('POST_ADDRESS',StringType(),True),
      StructField('CITY_NAME',StringType(),True),
      StructField('REGION_NAME',StringType(),True),
      StructField('COD_COUNTRY',StringType(),True),
      StructField('COD_LANGUAGE',StringType(),True),
      StructField('IS_BONO',BooleanType(),True),
      StructField('COD_STATE_USE',StringType(),True),
      StructField('USE_DATE',StringType(),True),
      StructField('CREATE_DATE',TimestampType(),True),
      StructField('MODIFY_DATE',TimestampType(),True),
      StructField('DELETE_DATE',TimestampType(),True),
      StructField('POST_CODE',StringType(),True),
      StructField('PHONE_MOB',StringType(),True),
      StructField('row_num',StringType(),True),
      StructField('ENABLE_ADVERTISING',BooleanType(),True),
      StructField('ENABLE_ADVERTISING_EMAIL',BooleanType(),True),
      StructField('ENABLE_ADVERTISING_PHONE',BooleanType(),True),
      StructField('ENABLE_ADVERTISING_APPS',BooleanType(),True),
      StructField('ENABLE_ADVERTISING_CUSTOMER_SEGMENTATION',BooleanType(),True),
      StructField('ENABLE_ADVERTISING_CROSSSELLING',BooleanType(),True),
      StructField('__index_level_0__',LongType(),True),
      StructField('ENABLE',BooleanType(),False)])
  
    self.test_assert_load(df, expected_schema)
    
class TestDW(TestMKSilver):
  # son class of TestMKSilver, created to provide a schema to use the method test_assert_load from TestMKSilver
  def test_dw(self, df):
    expected_schema = StructType([
      StructField('subscriberkey',StringType(),True),
      StructField('event_date',TimestampType(),True),
      StructField('interaction_type',StringType(),False),
      StructField('cod_park',NullType(),True)
      ])

    self.test_assert_load(df, expected_schema)
    
class TestLog(TestMKSilver):
  # son class of TestMKSilver, created to provide a schema to use the method test_assert_load from TestMKSilver
  def test_log(self, df):
    expected_schema = StructType([
      StructField('subscriberkey',StringType(),True),
      StructField('event_date',TimestampType(),True),
      StructField('interaction_type',StringType(),False),
      StructField('cod_park',StringType(),True)
      ])

    self.test_assert_load(df, expected_schema)