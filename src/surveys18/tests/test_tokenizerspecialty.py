from django.test import TestCase
from django.core.management import call_command
from surveys18.builder.tokenizer_specialty import Builder
from surveys18.builder.exceptions import SignError, StringLengthError, CreateModelError
from surveys18.models import (
    MarketType,
    IncomeRange,
    AnnualIncome,
    Survey,
    AddressMatch,
    Lack,
    FarmRelatedBusiness,
    Business,
    Phone,
    LandArea,
    LandType,
    LandStatus,
    Loss,
    Unit,
    Product,
    Contract,
    CropMarketing,
    LivestockMarketing,
    Facility,
    PopulationAge,
    Population,
    EducationLevel,
    FarmerWorkDay,
    LifeStyle,
    OtherFarmWork,
    Subsidy,
    RefuseReason,
    AgeScope,
    LongTermHire,
    ShortTermHire,
    WorkType,
    NumberWorkers,
    NoSalaryHire,
    ShortTermLack,
    LongTermLack,
    Gender,
    ProductType,
    Relationship,
    Month,
    Refuse
)


class ModelTestCase(TestCase):
    def setUp(self):
        call_command('loaddata', 'land-type.yaml', verbosity=0)
        call_command('loaddata', 'land-status.yaml', verbosity=0)
        call_command('loaddata', 'farm-related-business.yaml', verbosity=0)
        call_command('loaddata', 'management-type.yaml', verbosity=0)
        call_command('loaddata', 'product-type.yaml', verbosity=0)
        call_command('loaddata', 'product.yaml', verbosity=0)
        call_command('loaddata', 'loss.yaml', verbosity=0)
        call_command('loaddata', 'unit.yaml', verbosity=0)
        call_command('loaddata', 'contract.yaml', verbosity=0)
        call_command('loaddata', 'income-range.yaml', verbosity=0)
        call_command('loaddata', 'market-type.yaml', verbosity=0)
        call_command('loaddata', 'age-scope.yaml', verbosity=0)
        call_command('loaddata', 'gender.yaml', verbosity=0)
        call_command('loaddata', 'relationship.yaml', verbosity=0)
        call_command('loaddata', 'education-level.yaml', verbosity=0)
        call_command('loaddata', 'farmer-work-day.yaml', verbosity=0)
        call_command('loaddata', 'age-scope.yaml', verbosity=0)
        self.string = "16,106,100070416190,1,55,,3,賴武郎　　,0931668195 ,04-7583927 ,彰化縣線西鄉下犁村１７鄰下塭路５００巷９０號,,0,0,0,0,0,0,3,E999,其他農作___(請說明),2   ,100,6,1,72000,15,1,\"(短期蔬菜,小白菜,油菜，青江菜)\",1,3,F001,肉豬,3,0,1300,8400,0,,0,,,,,,,,,,,3,3,1,06800 ,6,7,"


        self.builder = Builder(self.string)
        self.builder.build_survey()

    def test_build_survey(self):
        obj = Survey.objects.get(farmer_id=self.builder.survey.farmer_id)
        self.assertEquals(obj.farmer_id, "100070416190")
        self.assertEquals(obj.page, 1)
        self.assertEquals(obj.total_pages, 1)
        self.assertEquals(obj.farmer_name, "賴武郎")

    def test_build_phone(self):
        self.builder.build_phone()
        obj = Phone.objects.filter(survey=self.builder.survey).all()
        self.assertEquals(obj[0].phone, "0931668195")
        self.assertEquals(obj[1].phone, "04-7583927")

    def test_build_address(self):
        self.builder.build_address()
        obj = AddressMatch.objects.get(survey=self.builder.survey)
        self.assertEquals(obj.match, False)
        self.assertEquals(obj.mismatch, True)
        self.assertEquals(obj.address, "彰化縣線西鄉下犁村１７鄰下塭路５００巷９０號")

    def test_build_land_area(self):
        self.builder.build_land_area()
        obj = LandArea.objects.filter(survey=self.builder.survey).all()
        self.assertEquals(len(obj[1]), 1)

        # self.assertEquals(obj[0].type.id, 1)
        # self.assertEquals(obj[0].status.id, 1)
        # self.assertEquals(obj[0].value, 100)

        # self.assertEquals(obj[1].type.id, 1)
        # self.assertEquals(obj[1].status.id, 2)
        # self.assertEquals(obj[1].value, 40)

    def test_build_business(self):
        self.builder.build_business()
        obj = Business.objects.filter(survey=self.builder.survey).all()
        self.assertEquals(len(obj), 0)
        # self.assertEquals(obj[0].farm_related_business, None)
        # self.assertEquals(obj[0].extra, "123")

    def test_build_management(self):
        self.builder.build_management()
        obj = Survey.objects.filter(farmer_id=self.builder.survey.farmer_id).all()
        self.assertEquals(len(obj), 0)
        # m_obj = obj[0].management_types.all()
        # self.assertEquals(m_obj[0].code, 14)

    def test_build_crop_marketing(self):
        self.builder.build_crop_marketing()
        obj = CropMarketing.objects.filter(survey=self.builder.survey).all()
        self.assertEquals(len(obj), 1)

    def test_build_livestock_marketing(self):
        self.builder.build_livestock_marketing()
        obj = LivestockMarketing.objects.filter(survey=self.builder.survey).all()
        self.assertEquals(len(obj), 1)

    def test_build_population(self):
        self.builder.build_population()
        obj = Population.objects.filter(survey=self.builder.survey).all()
        self.assertEquals(len(obj), 1)


