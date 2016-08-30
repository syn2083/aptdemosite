from django.db import models
from logging_setup import init_logging
from django.utils import timezone
from collections import OrderedDict
import json

logger = init_logging()


class DemoConfig(models.Model):
    id = models.AutoField(primary_key=True)
    jdf_input_path = models.CharField(verbose_name='JIF Input Folder', max_length=200,
                                      default='C:/APTApplication/Server/Inputs/JDFInput')
    reprint_path = models.CharField(verbose_name='Reprint Folder', max_length=200,
                                    default='C:/APTApplication/Server/Outputs/ReprintFiles')
    proc_phase_path = models.CharField(verbose_name='Processing Phase XML Folder', max_length=200,
                                       default='C:/APTApplication/Server/Outputs/WIP')
    jif_acks_path = models.CharField(verbose_name='JIF ACKs Folder', max_length=200,
                                     default='C:/APTApplication/Server/Inputs/JIFAcks')
    idc_1_path = models.CharField(verbose_name='IDC 1 Path', max_length=200, default='C:/APTApplication/IDC/IDC_1')
    idc_1_type = models.CharField(verbose_name='IDC 1 Device Type', max_length=40)
    idc_1_time = models.IntegerField(verbose_name='IDC 1 Scans per hour')
    idc_1_multi = models.IntegerField(verbose_name='IDC Multi-step', default=1)
    idc_1_ps = models.CharField(verbose_name='IDC 1 piece or sheet', default='sheet', max_length=5)
    idc_2_path = models.CharField(verbose_name='IDC 2 Path', max_length=200, default='C:/APTApplication/IDC/IDC_2')
    idc_2_type = models.CharField(verbose_name='IDC 2 Device Type', max_length=40)
    idc_2_time = models.IntegerField(verbose_name='IDC 2 Scans per hour')
    idc_2_ps = models.CharField(verbose_name='IDC 2 piece or sheet', default='sheet', max_length=5)
    idc_2_multi = models.IntegerField(verbose_name='IDC Multi-step', default=0)
    idc_3_path = models.CharField(verbose_name='IDC 3 Path', max_length=200, default='C:/APTApplication/IDC/IDC_3')
    idc_3_type = models.CharField(verbose_name='IDC 3 Device Type', max_length=40)
    idc_3_time = models.IntegerField(verbose_name='IDC 3 Scans per hour')
    idc_3_ps = models.CharField(verbose_name='IDC 3 piece or sheet', default='piece', max_length=5)
    idc_3_multi = models.IntegerField(verbose_name='IDC Multi-step', default=0)
    idc_4_path = models.CharField(verbose_name='IDC 4 Path', max_length=200, default='C:/APTApplication/IDC/IDC_4')
    idc_4_type = models.CharField(verbose_name='IDC 4 Device Type', max_length=40, default='reprint')
    idc_4_time = models.IntegerField(verbose_name='IDC 4 Scans per hour', default=12000)
    idc_4_ps = models.CharField(verbose_name='IDC 4 piece or sheet', default='piece', max_length=5)
    idc_4_multi = models.IntegerField(verbose_name='IDC Multi-step', default=0)
    idc_5_path = models.CharField(verbose_name='IDC 5 Path', max_length=200, default='C:/APTApplication/IDC/idc_5')
    idc_5_type = models.CharField(verbose_name='IDC 5 Device Type', max_length=40, default='reprint')
    idc_5_time = models.IntegerField(verbose_name='IDC 5 Scans per hour', default=12000)
    idc_5_ps = models.CharField(verbose_name='IDC 5 piece or sheet', default='piece', max_length=5)
    idc_5_multi = models.IntegerField(verbose_name='IDC Multi-step', default=0)
    idc_6_path = models.CharField(verbose_name='IDC 6 Path', max_length=200, default='C:/APTApplication/IDC/idc_6')
    idc_6_type = models.CharField(verbose_name='IDC 6 Device Type', max_length=40, default='reprint')
    idc_6_time = models.IntegerField(verbose_name='IDC 6 Scans per hour', default=12000)
    idc_6_ps = models.CharField(verbose_name='IDC 6 piece or sheet', default='piece', max_length=5)
    idc_6_multi = models.IntegerField(verbose_name='IDC Multi-step', default=0)
    td_path = models.CharField(verbose_name='TD Input Path', max_length=200, default='C:/APTApplication/IDC/TD')
    td_type = models.CharField(verbose_name='TD Device Type', max_length=40, default='inserter')
    td_ps = models.CharField(verbose_name='TD Piece or Sheet', max_length=5, default='piece')
    td_time = models.IntegerField(verbose_name='TD Scans per hour', default=12000)
    td_multi = models.IntegerField(verbose_name='TD Multi-step', default=0)
    td_multi_path = models.CharField(verbose_name='TD Input Path', max_length=200, default='C:/APTApplication/IDC/TD')
    active_targets = models.CharField(verbose_name='Active Targets', max_length=200, default='icd_1, icd_2, icd_3, td')
    reprint_pool = models.CharField(verbose_name='Reprint Pool', max_length=200, default='icd_4, icd_5, icd_6')
    all_targets = models.CharField(verbose_name='All Targets', max_length=200, default='icd_1, icd_2, icd_3, '
                                                                                       'icd_4, icd_5, icd_6td')

    def save_demo(self):
        self.save()
        logger.debug('Demo Settings Saved')

    def gen_json(self):
        icds = []
        icd_dict = OrderedDict()
        icd_1 = {i: v for i, v in self.__dict__.items() if i.startswith('idc_1')}
        icds.append(('icd_1', 'idc_1', icd_1))
        icd_2 = {i: v for i, v in self.__dict__.items() if i.startswith('idc_2')}
        icds.append(('icd_2', 'idc_2', icd_2))
        icd_3 = {i: v for i, v in self.__dict__.items() if i.startswith('idc_3')}
        icds.append(('icd_3', 'idc_3', icd_3))
        icd_4 = {i: v for i, v in self.__dict__.items() if i.startswith('idc_4')}
        icds.append(('icd_4', 'idc_4', icd_4))
        icd_5 = {i: v for i, v in self.__dict__.items() if i.startswith('idc_5')}
        icds.append(('icd_5', 'idc_5', icd_5))
        icd_6 = {i: v for i, v in self.__dict__.items() if i.startswith('idc_6')}
        icds.append(('icd_6', 'idc_6', icd_6))
        td = {i: v for i, v in self.__dict__.items() if i.startswith('td')}
        icds.append(('td', 'td', td))
        apt_dirs = {'APTDirs': {'JDF': self.jdf_input_path, 'JIFACK': self.jif_acks_path, 'PROC': self.proc_phase_path,
                                'REPRINT': self.reprint_path}}
        targets = {'active_targets': self.active_targets.split(','), 'reprint_pool': self.reprint_pool.split(','),
                   'all_targets': self.all_targets.split(',')}
        for icd in icds:
            t = OrderedDict()
            t['path'] = icd[2]['{}_path'.format(icd[1])]
            t['sph'] = icd[2]['{}_time'.format(icd[1])]
            t['piece_sheet'] = icd[2]['{}_ps'.format(icd[1])]
            t['multi_step'] = icd[2]['{}_multi'.format(icd[1])]
            t['jobid'] = []
            icd_dict[icd[0]] = t

        ol = []
        ol.append(icd_dict)
        ol.append(apt_dirs)
        ol.append(targets)

        return json.dumps(ol)


class JIFTemplate(models.Model):
    id = models.AutoField(primary_key=True)
    template_name = models.CharField(max_length=100, default='APTDemo')
    job_prefix = models.CharField(max_length=3)
    account_id = models.CharField(max_length=1000)
    job_name = models.CharField(max_length=1000)
    job_type = models.CharField(max_length=1000)
    job_number = models.CharField(max_length=1000)
    job_class = models.CharField(max_length=1000)
    product_name = models.CharField(max_length=1000)
    production_location = models.CharField(max_length=500)
    envelope_id = models.CharField(max_length=1000)
    stock_id = models.CharField(max_length=1000)
    stock_type = models.CharField(max_length=1000)
    user_info_1 = models.CharField(max_length=1000)
    user_info_2 = models.CharField(max_length=1000)
    user_info_3 = models.CharField(max_length=1000)
    user_info_4 = models.CharField(max_length=1000)
    user_info_5 = models.CharField(max_length=1000)
    contact_email = models.CharField(max_length=1000)
    # Options
    piece_range = models.CharField(max_length=100)
    shift_1_operators = models.CharField(max_length=500)
    shift_2_operators = models.CharField(max_length=500)
    shift_3_operators = models.CharField(max_length=500)
    template_date = models.DateTimeField(default=timezone.now)

    def save_jif(self):
        self.template_date = timezone.now()
        self.save()
        logger.debug('JIF Template Settings Saved')

    def __str__(self):
        return self.template_name
